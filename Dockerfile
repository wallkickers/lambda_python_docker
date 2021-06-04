FROM python:3
USER root

RUN apt-get update

ADD . /code
WORKDIR /code
RUN apt-get install -y vim less
RUN pip install --upgrade setuptools
