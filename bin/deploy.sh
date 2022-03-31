#!/bin/bash

git stash & git pull
docker-compose up --build --force-recreate -d
docker-compose exec -T bot alembic upgrade head