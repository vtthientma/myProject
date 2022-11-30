FROM python:3.7-alpine

WORKDIR /app

COPY *.py /app/

RUN apk update
RUN apk add build-base
RUN pip3 install -U pylint
# RUN pylint --max-line-length=250 --disable=C0325 *.py
CMD pylint --max-line-length=250 --disable=C0325 *.py
