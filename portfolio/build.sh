#!/bin/bash
docker build -t so2harbor.com:6000/library/svelte_app:latest --network=host .
docker push  so2harbor.com:6000/library/svelte_app:latest
