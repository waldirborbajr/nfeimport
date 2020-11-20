build:
	docker-compose -f docker-compose.prod.yaml --force-recreate --build

start:
	docker-compose -f docker-compose.prod.yaml up -d

stop:
	docker-compose -f docker-compose.prod.yaml down --remove-orphans

run:
	docker exec -it ct_python /bin/bash	

.PHONY: build