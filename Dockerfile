FROM python:3.11.4

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/bin/src/webapp

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

IMAGE_NAME = app.py

.PHONY: run-server docker-build

RUN_SERVER_CMD = flask run --host=0.0.0.0
DOCKER_BUILD_CMD = docker build -t $(IMAGE_NAME)

run-server:
@echo "starting flask server"
$(RUN_SERVER_CMD)

docker-build:
@echo "building docker image"
$(DOCKER_BUILD_CMD)
