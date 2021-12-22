

IP=$1
PORT=$2
INTERVAL=$3

while true;
do
    curl -d '[
        {"Age": 85, "Sex": "male", "Embarked": "S"},
        {"Age": 24, "Sex": "female", "Embarked": "C"},
        {"Age": 3, "Sex": "male", "Embarked": "C"},
        {"Age": 21, "Sex": "male", "Embarked": "S"}
    ]' -H "Content-Type: application/json" \
       -X POST http://$IP:$PORT/predict 
    sleep $INTERVAL
done