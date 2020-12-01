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

.PHONY: default

default: help

production: stop dang rebuild deploy

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

dang:
	@echo "\nStarting dangling removal\n"
	docker rmi $$(docker images -q -f dangling=true)

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

prune:
	docker system prune -a -f --volumes

help:
	@echo ''
	@echo 'Usage: make [TARGET] [EXTRA_ARGUMENTS]'
	@echo 'Targets:'
	@echo '  build    	build docker --image-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  rebuild  	rebuild docker --image-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  test     	test docker --container-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  service   	run as service --container-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  login   	run as service and login --container-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  clean    	remove docker --image-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  prune    	shortcut for docker system prune -af. Cleanup inactive containers and cache.'
	@echo '  shell      run docker --container-- for current user: $(HOST_USER)(uid=$(HOST_UID))'
	@echo ''
	@echo 'Extra arguments:'
	@echo 'cmd=:	make cmd="whoami"'
	@echo '# user= and uid= allows to override current user. Might require additional privileges.'
	@echo 'user=:	make shell user=root (no need to set uid=0)'
	@echo 'uid=:	make shell user=dummy uid=4000 (defaults to 0 if user= set)'

# 	docker container rm $$(docker ps -aq) -f
# 	docker image rm $$(docker images --format "{{.ID}}" --filter "dangling=true")
# 	docker volume ls -f dangling=true

# $ docker run -dt <image>
# $ docker exec -it <container> <command>

# docker run -dt --name nfeimport wborbajr/nfeimport:latest
# docker exec -it nfeimport /bin/bash
