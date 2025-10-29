#!/usr/bin/env python3
"""
Vulnerable code example: Server-Side Request Forgery (SSRF)
This code is intentionally vulnerable for testing purposes.
"""

import requests
import urllib.request
from flask import Flask, request

app = Flask(__name__)

@app.route('/fetch_url')
def fetch_url():
    url = request.args.get('url')
    
    # VULNERABLE: SSRF - Fetching arbitrary URLs
    response = requests.get(url)
    return response.text

@app.route('/proxy')
def proxy():
    target = request.args.get('target')
    
    # VULNERABLE: SSRF via proxy
    with urllib.request.urlopen(target) as response:
        content = response.read()
    return content

@app.route('/webhook')
def webhook():
    callback_url = request.args.get('callback')
    
    # VULNERABLE: SSRF via webhook
    data = {'status': 'completed'}
    response = requests.post(callback_url, json=data)
    return f"Webhook sent: {response.status_code}"

@app.route('/check_url')
def check_url():
    url = request.args.get('url')
    
    # VULNERABLE: SSRF - URL validation bypass
    try:
        response = requests.head(url, timeout=5)
        return f"URL is reachable: {response.status_code}"
    except:
        return "URL is not reachable"

@app.route('/fetch_image')
def fetch_image():
    image_url = request.args.get('url')
    
    # VULNERABLE: SSRF via image fetching
    response = requests.get(image_url)
    return response.content, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)

