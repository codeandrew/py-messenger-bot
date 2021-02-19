#!/bin/bash

COUNTER=$1
SUBPATH="add_row"
DOMAIN=http://0.0.0.0:8080
URL="${DOMAIN}/${SUBPATH}"

JSON='[{ "message": "hello" }]'

echo $URL
curl -d "$JSON" -H 'Content-Type: application/json' $URL
