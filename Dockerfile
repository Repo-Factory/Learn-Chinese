#syntax=docker/dockerfile:

# pynput won't work properly with linux base image, I don't have the system 
# requirements to use windows hypervisor to access windows docker base image
FROM winamd64/python:3

WORKDIR C:\Users\Conner\PycharmProjects\learn-chinese

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python -m install pynput

RUN pip install lxml

COPY . C:\Users\Conner\PycharmProjects\learn-chinese

ENV PYTHONPATH "${PYTHONPATH}:C:\Users\Conner\PycharmProjects\learn-chinese"

CMD [ "python", "m", "app.main", "--host=0.0.0.0"]


