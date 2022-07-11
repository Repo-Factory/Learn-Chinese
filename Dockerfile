#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /C:\Users\Conner\PycharmProjects\learn-chinese\app.app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "m", "app.app", "--host=0.0.0.0"]