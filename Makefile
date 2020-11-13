VOLUME_NAME ?= www-le-taxi-cache-bundle


local: create-volume
	docker run -p 4000:4000 -v ${VOLUME_NAME}:/usr/local/bundle -v `pwd`:/site bretfisher/jekyll-serve

shell: create-volume
	docker run -ti -p 4000:4000 -v ${VOLUME_NAME}:/usr/local/bundle -v `pwd`:/site --entrypoint bash bretfisher/jekyll-serve

create-volume:
	docker volume create ${VOLUME_NAME}

destroy-volume:
	docker volume rm ${VOLUME_NAME}
