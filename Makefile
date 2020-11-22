PROJECT = lightjar
ID = pikesley/${PROJECT}

all: build

build:
	docker build \
		--tag ${ID} .

run:
	docker-compose exec ${PROJECT} bash
