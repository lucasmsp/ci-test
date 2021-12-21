FROM python:3.7.3-alpine3.9
LABEL maintainer="Lucas Ponce <lucasmsp@dcc.ufmg.br>"

RUN apk add --no-cache gcc g++

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "test.py", "9999" ]
