#!/bin/bash
ENV=$1

echo "Deploying to $ENV environment"

docker-compose pull
docker-compose down
docker-compose up -d

echo "Verifying deployment"
curl http://localhost:5000/health
