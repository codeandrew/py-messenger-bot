#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask Setup
import os, sys
import requests
from datetime import datetime
from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from pprint import pprint

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

verify_token = 'hello'
@app.route('/', methods=["GET"])
def verify():
    # Webhook configuration
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == verify_token:
            return "Verification token mismatch", 403
    return request.args["hub.challenge"], 200

@app.route('/', methods=["POST"])
def webhook():
    data = request.get_json()
    log(data)

    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 8080))
