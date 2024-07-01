from flask import Blueprint, jsonify, request, session, url_for, redirect
from utils.zoom_client import load_token
import requests

update_meeting_bp = Blueprint('update_meeting', __name__)

@update_meeting_bp.route('/update_meeting/<meeting_id>', methods=['PATCH'])
def update_meeting(meeting_id):
    token = load_token()
    tok = token['access_token']

    if not token:
        return redirect(url_for('login'))

    headers = {
        "Authorization" : f"Bearer {tok}",
        'Accept': 'application/json'
    }

    base_url = 'https://api.zoom.us/v2'
    url = f'{base_url}/meetings/{meeting_id}'

    meeting_data = request.json()
    result = requests.patch(url, json=meeting_data,headers=headers)

    return jsonify(result.json())
