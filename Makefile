develop:
	docker-compose up --force-recreate --build && docker-compose down --remove-orphans

build:
	docker-compose -f docker-compose.prod.yaml build

test:
	docker-compose -f docker-compose.prod.yaml up --build --force-recreate
	docker-compose -f docker-compose.prod.yaml down --remove-orphans

start:
	docker-compose -f docker-compose.prod.yaml up -d

restart:
	docker-compose -f docker-compose.prod.yaml restart

pause:
	docker-compose -f docker-compose.prod.yaml pause

unpause:
	docker-compose -f docker-compose.prod.yaml unpause

stop:
	docker-compose -f docker-compose.prod.yaml down --remove-orphans

top:
	docker-compose -f docker-compose.prod.yaml top

ps:
	docker-compose -f docker-compose.prod.yaml ps

logs:
	docker-compose -f docker-compose.prod.yaml logs

events:
	docker-compose -f docker-compose.prod.yaml events

exec:
	docker exec -ti ct_python /bin/bash

run:
	docker run -t nfeimport

.PHONY: build

# $ docker run -dt <image>
# $ docker exec -it <container> <command>