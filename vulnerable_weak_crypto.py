#!/usr/bin/env python3
"""
Vulnerable code example: Weak Cryptography
This code is intentionally vulnerable for testing purposes.
"""

import hashlib
import random
from Crypto.Cipher import DES
from flask import Flask, request, session

app = Flask(__name__)

# VULNERABLE: Weak secret key
app.secret_key = '12345'

# VULNERABLE: Hardcoded encryption key
ENCRYPTION_KEY = b'weakkey1'

@app.route('/hash_password')
def hash_password():
    password = request.args.get('password')
    
    # VULNERABLE: Using MD5 for password hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    return f"Hashed password: {hashed}"

@app.route('/encrypt_data')
def encrypt_data():
    data = request.args.get('data')
    
    # VULNERABLE: Using DES encryption (weak algorithm)
    cipher = DES.new(ENCRYPTION_KEY, DES.MODE_ECB)
    padded_data = data + ' ' * (8 - len(data) % 8)
    encrypted = cipher.encrypt(padded_data.encode())
    return encrypted.hex()

@app.route('/generate_token')
def generate_token():
    # VULNERABLE: Weak random number generation
    token = random.randint(1000, 9999)
    return str(token)

@app.route('/hash_data')
def hash_data():
    data = request.args.get('data')
    
    # VULNERABLE: Using SHA1 (deprecated)
    hashed = hashlib.sha1(data.encode()).hexdigest()
    return hashed

@app.route('/create_session')
def create_session():
    username = request.args.get('user')
    
    # VULNERABLE: Predictable session token
    session['token'] = hashlib.md5(username.encode()).hexdigest()
    return "Session created"

# VULNERABLE: Exposed AWS credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABLE: Exposed API key
API_KEY = "sk-1234567890abcdef1234567890abcdef"

if __name__ == '__main__':
    app.run(debug=True)

