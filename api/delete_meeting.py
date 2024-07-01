from flask import Blueprint, jsonify, request, session, url_for, redirect
from utils.zoom_client import load_token
import requests

delete_meeting_bp = Blueprint('delete_meeting', __name__)

@delete_meeting_bp.route('/delete_meeting/<meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
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

    result = requests.delete(url, headers=headers)

    return jsonify(result.json())
