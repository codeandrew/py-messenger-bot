#!/bin/bash
IMAGE=pymessenger-hashmeer:1.0.0

docker build -t $IMAGE  .
docker run -p 8080 $IMAGE