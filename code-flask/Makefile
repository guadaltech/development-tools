#!make

CONTAINER_REPO:=tedezed
CONTAINER_IMAGE:=image-generator
CONTAINER_VERSION:=latest

build:
	docker build -f Dockerfile -t ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION} .

push:
	docker push ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION}

gcloud-push:
	gcloud docker -- push ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION}

build-no-cache:
	docker build -f Dockerfile -t ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION} --no-cache .

save:
	docker save ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION} -o ${CONTAINER_IMAGE}-${CONTAINER_VERSION}.docker

run:
	docker run -p 5000:5000 -p 5678:5678 ${CONTAINER_REPO}/${CONTAINER_IMAGE}:${CONTAINER_VERSION}

start:
	sudo chown ${USER} -R code
	sudo chmod 775 -R code
	docker-compose -f local.yaml up

dev:
	docker-compose -f dev.yaml up

prod:
	docker-compose -f prod.yaml up

all: build
