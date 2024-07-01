from flask import Blueprint, jsonify, request, session, url_for, redirect
import requests
from utils.zoom_client import load_token

create_meeting_bp = Blueprint('create_meeting', __name__)

@create_meeting_bp.route('/create_meeting/<user_id>', methods=['POST'])
def create_meeting(user_id):
    token = load_token()
    tok = token['access_token']

    if not token:
        return redirect(url_for('login'))

    headers = {
        "Authorization" : f"Bearer {tok}",
        'Accept': 'application/json'
    }

    base_url = 'https://api.zoom.us/v2'
    url = f'{base_url}/users/{user_id}/meetings'
    meeting_data = request.json()

    result = requests.post(url, headers=headers, json=meeting_data)

    return jsonify(result.json())
