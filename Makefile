#
#
#

# include docker.env

ifeq ($(user),)
	# USER retrieved from env, UID from shell.
	HOST_USER ?= $(strip $(if $(USER),$(USER),nodummy))
	HOST_UID ?= $(strip $(if $(shell id -u),$(shell id -u),4000))
else
	# allow override by adding user= and/ or uid=  (lowercase!).
	# uid= defaults to 0 if user= set (i.e. root).
	HOST_USER = $(user)
	HOST_UID = $(strip $(if $(uid),$(uid),0))
endif

PROJECT_NAME = nfeimport
DOCKER_USER = wborbajr
DOCKER_TAG = latest
# DOCKER_TAG := $(shell date +%Y%m%d)
DOCKERFILE = docker-compose.prod.yaml
CONTAINER = ${PROJECT_NAME}_$(HOST_UID)

export PROJECT_NAME
export DOCKER_TAG
export DOCKER_USER
export CONTAINER

.PHONY = build

build:
	@echo "\nStarting build...\n"
	docker-compose -f ${DOCKERFILE} build

rebuild:
	@echo "\nForcing Rebuild...\n"
	docker-compose -f ${DOCKERFILE} build --no-cache --force-rm --pull

start:
	@echo "\nStarting container...\n"
	docker-compose -f ${DOCKERFILE} up -d

stop:
	@echo "\nStoping container...\n"
	docker-compose -f ${DOCKERFILE} down --remove-orphans --rmi all

exec:
	@echo "\nEntering container...\n"
	docker exec -ti ${CONTAINER} /bin/bash

deploy:
	@echo "\nStarting delpoy...\n"
	docker push ${DOCKER_USER}/${PROJECT_NAME}:${DOCKER_TAG}

develop:
	docker-compose up --force-recreate --build && docker-compose down --remove-orphans

restart:
	docker-compose -f ${DOCKERFILE} restart

pause:
	docker-compose -f ${DOCKERFILE} pause

unpause:
	docker-compose -f ${DOCKERFILE} unpause

top:
	docker-compose -f ${DOCKERFILE} top

ps:
	docker-compose -f ${DOCKERFILE} ps

logs:
	docker-compose -f ${DOCKERFILE} logs

events:
	docker-compose -f ${DOCKERFILE} events

run:
	docker run -t nfeimport

prune:
	docker system prune -af

dang:
	docker volume ls -f dangling=true
	# docker image rm $(docker images --format "{{.ID}}" --filter "dangling=true")

# $ docker run -dt <image>
# $ docker exec -it <container> <command>

# docker run -dt --name nfeimport wborbajr/nfeimport:latest
# docker exec -it nfeimport /bin/bash
