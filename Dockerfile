FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y \
    net-tools \
    ncat \
    && pip install interruptingcow \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir app
COPY challenges/misc/guess-passwd/task.py app/task.py
COPY challenges/misc/guess-passwd/flag.txt app/flag.txt
COPY challenges/misc/guess-passwd/start_nc.sh app/start_nc.sh

WORKDIR /app