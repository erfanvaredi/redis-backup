include .env

lint:
	black . 

run_api: 
	uvicorn api_runner:app --host 0.0.0.0 --port 6561

run_test:
	@echo "not implemented"

start:
	docker-compose -f docker-compose.yaml up -d
stop:
	docker-compose -f docker-compose.yaml down -v
clear:
	docker rmi redis-backup-api:${VERSION}
	echo y | docker container prune
	echo y | docker image prune

restart_api:
	docker stop redis-backup-api
	echo y | docker container prune
	docker rmi redis-backup-api:"${VERSION}"
	docker build -f api.Dockerfile -t redis-backup-api:"${VERSION}" .
	docker run -d -p 6561:6561 redis-backup-api:"${VERSION}"
