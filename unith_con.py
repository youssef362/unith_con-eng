from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
HEADERS={'Content-Type': 'application/json'}
BOT_WEBHOOK='https://webhook.site/b03c80bf-6ae0-4222-bd81-4725376b81a8'

@app.route('/conversation', methods=['post'])
def get_bot_answer():
    incomingdata=request.json
    print('indata=', incomingdata)
    print('indatazero=', incomingdata[0]['payload']['message'])   
    bot_response = requests.post(BOT_WEBHOOK, headers = HEADERS, params = {'event': 'new_message', 'chat': {'id': 'some_id'},'text': incomingdata[0]['payload']['message']}).json()
    print('bot_response= ', bot_response)
    resp = {[{'type': 'text', 'payload': {'type': 'text', 'message': bot_response['messages'][0]['text']}}]} 
    return resp

if __name__ == '__main__':
    app.run()
