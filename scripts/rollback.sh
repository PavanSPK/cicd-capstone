#!/bin/bash
echo "Rollback initiated"
docker-compose down
docker-compose up -d
