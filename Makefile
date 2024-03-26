IMAGE_NAME = app.py
	
RUN_SERVER_CMD = flask run --host=0.0.0.0 --port=8080
DOCKER_BUILD_CMD = docker build -t $(IMAGE_NAME)

run-server:
	@echo "starting flask server"
	$(RUN_SERVER_CMD)

docker-build:
	@echo "building docker image"
	$(DOCKER_BUILD_CMD)