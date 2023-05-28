FROM python:3.8 as base

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip

