FROM python:3.8-slim-buster

LABEL maintainer="Lucas Ponce <lucasmsp@dcc.ufmg.br>"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && pip3 install  --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "/app/test.py", "9999" ]
