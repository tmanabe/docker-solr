#!/bin/bash

docker build -t solr:9.2.1 ./solr
docker run -d --name solr -p 5005:5005 -p 8983:8983 solr:9.2.1
