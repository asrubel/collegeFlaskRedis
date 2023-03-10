up:
	sudo docker-compose --env-file ./.env.list up
up_silent:
	sudo docker-compose --env-file ./.env.list up -d

up_redis:
	sudo docker-compose --env-file ./.env.list up redis
up_silent_redis:
	sudo docker-compose --env-file ./.env.list up -d redis

show:
	sudo docker ps
show_all:
	sudo docker ps -a
exec_web:
	sudo docker exec -it collegeflaskredis_web_1 sh

clean:
	sudo docker-compose --env-file ./.env.list down
	sudo docker image prune -a
	sudo docker volume prune
