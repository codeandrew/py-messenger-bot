#!/bin/bash
PAGE_ACCESS_TOKEN="EAANyTNnKofkBALhX9NY1ltJ3UYSMopHGUGqL4rLaPAZBfZBDJwNFIUVosfnUuOwMzzZBiBYEbRPwo7PXCEUX645EZBoZB94h6czxjC8vxh16qiZClCuvpbbqQX9uXpVXbsua6yT8cTlDEnWyrTYPsm7KxtCZBxjG4Dae1PM1T3xBfkhIVnJdjjC"

curl -i -X GET "https://graph.facebook.com/v9.0/me/messaging_feature_review?access_token=${PAGE_ACCESS_TOKEN}"