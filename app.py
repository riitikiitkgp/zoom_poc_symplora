import os
import json
from flask import Flask, Blueprint, jsonify, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from utils.zoom_client import load_token
import base64, requests

from api.create_meeting import create_meeting_bp
from api.get_meeting import get_meeting_bp
from api.update_meeting import update_meeting_bp
from api.delete_meeting import delete_meeting_bp
from api.list_meetings import list_meetings_bp

app = Flask(__name__)
app.secret_key = "aafa11332e7047a9b4039a50cd736ca3790df50b677ff5704e6d12b91c71e102"

app.register_blueprint(create_meeting_bp)
app.register_blueprint(get_meeting_bp)
app.register_blueprint(update_meeting_bp)
app.register_blueprint(delete_meeting_bp)
app.register_blueprint(list_meetings_bp)

oauth = OAuth(app)

zoom = oauth.register(
    name='zoom',
    client_id='9SD8anEwRy2xtRBmw866lg',
    client_secret='wHdjsPr2ZHfqwZCAXGoDreY4F90O9cXs',
    authorize_url='https://zoom.us/oauth/authorize',
    authorize_params=None,
    access_token_url='https://zoom.us/oauth/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:4001/authorize',
    client_kwargs={'scope': 'meeting:read:meeting:admin meeting:read:list_meetings:admin meeting:read:participant:admin meeting:update:meeting:admin  meeting:delete:meeting:admin meeting:write:meeting:admin'}
)

account_id = 'a4z2VxusRZmg-k-C8d6quw'

@app.route('/login')
def get_access_token():
    credentials = f"{zoom.client_id}:{zoom.client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    # Set up the body of the request
    data = {
        "grant_type": "account_credentials",
        "account_id": account_id
    }

    response = requests.post('https://zoom.us/oauth/token', headers=headers, data=data)

    if response.status_code == 200:
        token_data = response.json()

        with open('token.json', 'w') as token_file:
            json.dump(token_data, token_file)
        return jsonify(token_data)
    else:
        return jsonify({"error": "Failed to get access token", "details": response.json()}), response.status_code


@app.route('/')
def index():
    return "Welcome to Zoom API Integration!"

if __name__ == '__main__':
    app.run(port=4001, debug=True)
