#!/usr/bin/env python3
"""
Vulnerable code example: Path Traversal
This code is intentionally vulnerable for testing purposes.
"""

import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    filename = request.args.get('file')
    
    # VULNERABLE: Path Traversal
    file_path = os.path.join('/var/www/files/', filename)
    return send_file(file_path)

@app.route('/read_file')
def read_file():
    filename = request.args.get('name')
    
    # VULNERABLE: Path Traversal
    with open(f"./uploads/{filename}", 'r') as f:
        content = f.read()
    return content

@app.route('/get_log')
def get_log():
    log_file = request.args.get('log')
    
    # VULNERABLE: Path Traversal
    path = "/var/log/" + log_file
    with open(path, 'r') as f:
        return f.read()

@app.route('/view_image')
def view_image():
    image = request.args.get('img')
    
    # VULNERABLE: Path Traversal
    image_path = "static/images/" + image
    return send_file(image_path)

@app.route('/delete_file')
def delete_file():
    filename = request.args.get('file')
    
    # VULNERABLE: Path Traversal + File Deletion
    filepath = os.path.join('./temp/', filename)
    os.remove(filepath)
    return "File deleted"

if __name__ == '__main__':
    app.run(debug=True)

