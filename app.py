#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask Setup
import os, sys
import requests
from datetime import datetime
from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from pprint import pprint
from pymessenger import Bot

PAGE_ACCESS_TOKEN = "ACCESSTOKEN"
bot = Bot(PAGE_ACCESS_TOKEN)

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

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                sender_id = messaging_event['sender']['id']
                receipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text'] + " #echo"
                    else:
                        messaging_text = 'no text'

                    # Echo 
                    response = messaging_text
                    bot.send_text_message(sender_id, response)
    return "hello", 200

def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 8080))
