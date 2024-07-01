import requests
import json
import os

def load_token():
    if os.path.exists('token.json'):
        with open('token.json', 'r') as f:
            return json.load(f)
    return None