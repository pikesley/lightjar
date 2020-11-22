FROM python:3.7

RUN apt-get update && apt-get install -y make rsync

ENV PROJECT lightjar

COPY docker-config/bashrc /root/.bashrc

WORKDIR /opt/${PROJECT}

