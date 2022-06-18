#!/bin/bash

docker build -t solr:8.11.1 ./solr
docker run -d --name solr -p 5005:5005 -p 8983:8983 solr:8.11.1
