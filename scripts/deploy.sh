#!/bin/bash

ENV=$1

if [ -z "$ENV" ]; then
  echo "Usage: ./deploy.sh <dev|staging|prod>"
  exit 1
fi

ENV_FILE=".env.$ENV"

if [ ! -f "$ENV_FILE" ]; then
  echo "Environment file $ENV_FILE not found!"
  exit 1
fi

echo "Deploying to $ENV environment using $ENV_FILE"

docker compose --env-file $ENV_FILE pull
docker compose --env-file $ENV_FILE down
docker compose --env-file $ENV_FILE up -d

echo "Verifying deployment for $ENV"
docker-compose exec -T backend curl -sf http://localhost:5000/health

echo "Deployment successful for $ENV"
