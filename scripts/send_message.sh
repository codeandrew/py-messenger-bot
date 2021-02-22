#!/bin/bash
set -x
source ./config.sh


curl -X POST $MESSAGES_API_URL \
  -H 'Authorization: Bearer '$JWT'\
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d $'{
    "from": { "type": "messenger", "id": "'$FB_SENDER_ID'" },
    "to": { "type": "messenger", "id": "'$FB_RECIPIENT_ID'" },
    "message": {
      "content": {
        "type": "text",
        "text": "This is a Facebook Messenger Message sent from the Messages API"
      }
    }
  }'
