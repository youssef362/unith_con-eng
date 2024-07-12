from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
HEADERS={'Content-Type': 'application/json'}
BOT_WEBHOOK='https://admin.chatme.ai/connector/webim/webim_message/a1a4d7a9976dc3461271f0515d587ad0/bot_api_webhook'
WEBHOOK_SITE='https://webhook.site/b03c80bf-6ae0-4222-bd81-4725376b81a8'

@app.route('/conversation', methods=['post'])
def get_bot_answer():
    incomingdata=request.json
    print('indata=', incomingdata)
    print('indatazero=', incomingdata[0]['payload']['message'])   
    ###whs = requests.post(WEBHOOK_SITE, headers = HEADERS, json = {'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']})
    ###bot_response = requests.post(BOT_WEBHOOK, headers = HEADERS, json = {'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']})
    bot_response = requests.request("POST", BOT_WEBHOOK, headers=HEADERS, json={'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']})
    whs = requests.request("POST", WEBHOOK_SITE, headers=HEADERS, json={'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']})
    print('bot_response= ', bot_response.content)
    json_bot_response= json.dumps(bot_response.content.decode('utf-8'))
    json_bot_response = json.loads(json_bot_response)
    print('json_bot_response= ', json_bot_response)
    print('json_bot_response.json= ', json_bot_response.json)
    resp = {[{'type': 'text', 'payload': {'type': 'text', 'message': json_bot_response.json['messages'][0]['text']}}]} 
    return resp

if __name__ == '__main__':
    app.run()
