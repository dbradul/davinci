#!/bin/sh

while :; do
	echo "Starting server..."
	pipenv run python src/main.py     # run in foreground
	sleep 5
done
