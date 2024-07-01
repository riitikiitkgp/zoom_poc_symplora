from flask import Blueprint, jsonify, request, session, url_for, redirect
from utils.zoom_client import load_token
import requests

get_meeting_bp = Blueprint('get_meeting', __name__)

@get_meeting_bp.route('/get_meeting/<meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    # token = load_token()
    token = load_token()
    tok = token['access_token']

    if not token:
        return redirect(url_for('login'))

    # if not token:
    #     return redirect(url_for('login'))

    headers = {
        "Authorization" : f"Bearer {tok}",
        'Accept': 'application/json'
    }

    base_url = 'https://api.zoom.us/v2'
    url = f'{base_url}/meetings/{meeting_id}'

    result = requests.get(url, headers=headers)
    return jsonify(result.json())
