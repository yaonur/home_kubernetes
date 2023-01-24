#!/bin/bash
sudo docker build -t so2harbor.com:6000/library/portfolio:latest --network=host .
sudo docker push  so2harbor.com:6000/library/portfolio:latest
