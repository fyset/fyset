FROM python:3.6-alpine

# Sources
RUN mkdir -p /app

COPY ./requirements.txt /app/
WORKDIR /app

RUN apk add --update bash linux-headers musl-dev postgresql-dev gcc

RUN pip install -r requirements.txt
