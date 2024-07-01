from flask import Blueprint, jsonify, request, session, url_for, redirect
import requests
from utils.zoom_client import load_token

create_invite_link_bp = Blueprint('create_invite_link', __name__)

@create_invite_link_bp.route('/meetings/<meeting_id>/invite_links', methods=['POST'])
def create_invite_link(meeting_id):
    token = load_token()
    tok = token['access_token']

    if not token:
        return redirect(url_for('login'))

    headers = {
        "Authorization" : f"Bearer {tok}",
        'Accept': 'application/json'
    }

    base_url = 'https://api.zoom.us/v2'
    url = f'{base_url}/meetings/{meeting_id}/invite_links'
    meeting_data = request.json()

    result = requests.post(url, headers=headers, json=meeting_data)

    return jsonify(result.json())
