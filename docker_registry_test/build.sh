#!/bin/bash
#docker rmi docker_registry_test -f
#docker build -t docker_registry_test:latest --network=host .
docker build -t so2harbor.com/library/docker_registry_test:latest --network=host .
docker push  so2harbor.com/library/docker_registry_test:latest
#docker push r:latest
