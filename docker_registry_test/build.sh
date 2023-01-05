#!/bin/bash
docker rmi docker_registry_test -f
docker build -t docker_registry_test:latest --network=host .
#docker push r:latest
