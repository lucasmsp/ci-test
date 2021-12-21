FROM python:3.8-slim-buster

LABEL maintainer="Lucas Ponce <lucasmsp@dcc.ufmg.br>"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY . /app

RUN pip3 install  --no-cache-dir -r requirements.txt


ENTRYPOINT [ "python3" ]

CMD [ "test.py", "9999" ]
