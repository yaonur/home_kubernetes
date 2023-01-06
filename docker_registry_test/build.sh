#!/bin/bash
docker rmi docker_registry_test -f
#docker build -t docker_registry_test:latest --network=host .
docker build -t reg.so2harbor.com/docker_registry_test:latest --network=host .
docker push  reg.so2harbor.com/docker_registry_test:latest
#docker push r:latest
