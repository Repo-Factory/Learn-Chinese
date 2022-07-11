#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR C:\Users\Conner\PycharmProjects\learn-chinese

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python -m install pynput

RUN pip install lxml

COPY . C:\Users\Conner\PycharmProjects\learn-chinese

ENV PYTHONPATH "${PYTHONPATH}:C:\Users\Conner\PycharmProjects\learn-chinese"

CMD [ "python", "m", "app.main", "--host=0.0.0.0"]


