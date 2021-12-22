import sys
import os
import urllib.request
import traceback
from datetime import datetime
from icecream import ic 
import time
import socket

from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

def time_format():
    return f'{datetime.now()}|> '

ic.configureOutput(prefix=time_format, includeContext=True)

# inputs
training_data = 'data/titanic.csv'
include = ['Age', 'Sex', 'Embarked', 'Survived']
dependent_variable = include[-1]

model_file_name = os.environ["url_model"]
model_columns_file_name = os.environ["url_column_model"]
version_model = os.environ["version_model"]

model_columns = None
clf = None
hostname = socket.gethostname()

@app.route('/predict', methods=['POST'])
def predict():
    if clf:
        try:
            json_ = request.json
            ic("Received request: ", json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(clf.predict(query))

            output = jsonify({"prediction": list(map(int, prediction)), 
                              "version": version_model, 
                              "hostname": hostname})
            ic("Sending output: ", output)
            return output

        except Exception as e:
            output = jsonify({'error': str(e), 'trace': traceback.format_exc()})
            ic("Sending output: ", output)
            return output
    else:
        ic("No model found")
        return 'No model found'

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    try:
        clf = joblib.load(urllib.request.urlopen(model_file_name))
        print('model loaded')
        model_columns = joblib.load(urllib.request.urlopen(model_columns_file_name))
        print('model columns loaded')

    except Exception as e:
        print('No model here')
        print('Train first')
        print(str(e))
        clf = None

    app.run(host='0.0.0.0', port=port, debug=True)
