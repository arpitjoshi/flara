FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./src /app

ENV SIMPLE_SETTINGS=settings_common

EXPOSE 5000

