build:
	docker-compose -f docker-compose.prod.yaml build

start:
	docker-compose -f docker-compose.prod.yaml up -d

test:
	docker-compose -f docker-compose.prod.yaml up

stop:
	docker-compose -f docker-compose.prod.yaml down --remove-orphans

run:
	docker exec -it ct_python /bin/bash	

.PHONY: build