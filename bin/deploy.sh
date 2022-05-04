#!/bin/bash

git stash & git pull
docker-compose up --build --force-recreate -d