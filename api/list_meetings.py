from flask import Blueprint, jsonify, request, session, url_for, redirect
from utils.zoom_client import load_token
import requests

list_meetings_bp = Blueprint('list_meetings', __name__)

@list_meetings_bp.route('/users/<user_id>/list_meetings', methods=['GET'])
def list_meetings(user_id):
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

    result = requests.get(url, headers=headers)

    return jsonify(result.json())
