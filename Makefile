.DEFAULT_GOAL := default

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# ----------------------------------------------------------------------------------------------------------------------
.PHONY: help start stop restart ps prune


default: help

help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

start: ## Start service
	./run.sh

copy_to: ## Copy db to aws
	scp -i ~/.ssh/main_sunday.pem ./data/database.sqlite3 ubuntu@myaws_sunday2:/home/ubuntu/davinci/data/database.sqlite3

copy_from: ## Copy db from aws
	scp -i ~/.ssh/main_sunday.pem ubuntu@myaws_sunday2:/home/ubuntu/davinci/data/database.sqlite3 ./data/database.sqlite3

tests: ## Run tests
	pytest -s -v ./src/tests --setup-show

testn: ## Run test by its n=<name>
	pytest -s -v ./src/tests/test_solutions.py::{n} --setup-show

export: ## Export env variables
	export $(cat .env | sed 's/#.*//g' | xargs)
