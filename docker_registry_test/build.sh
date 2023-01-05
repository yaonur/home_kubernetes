#!/bin/bash
docker build -t docker_registry_test:latest --network=host .
#docker push r:latest
