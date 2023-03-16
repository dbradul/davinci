#!/bin/sh

while :; do
	echo "Starting server..."
	pipenv run python src/main.py     # run in background
	sleep 5
done
