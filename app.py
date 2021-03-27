from flask import Flask, request
from flask_cors import CORS
import os
from twilio.rest import Client

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Portfolio Notifier'


@app.route('/api/sendSms', methods=['POST'])
def send_sms():
    request_body = request.get_json()
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #              body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    #              from_='+16505347403',
    #              to='+12488262294')
    print(request_body)
    return {"message": "success"}


app.run(port=5000)
