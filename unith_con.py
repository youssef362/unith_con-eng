from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
HEADERS={'Content-Type': 'application/json'}
BOT_WEBHOOK='https://admin.chatme.ai/connector/webim/webim_message/a1a4d7a9976dc3461271f0515d587ad0/bot_api_webhook'

@app.route('/conversation', methods=['post'])
def get_bot_answer():
    incomingdata=request.json
    print(incomingdata)
    bot_response = requests.post(BOT_WEBHOOK, HEADERS, params = {'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']}).json()
    print(bot_response)
    resp = {[{'type': 'text', 'payload': {'type': 'text', 'message': bot_response['messages'][0]['text']}}]} 
    return resp

if __name__ == '__main__':
    app.run()
