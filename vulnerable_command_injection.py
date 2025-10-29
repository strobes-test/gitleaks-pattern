#!/usr/bin/env python3
"""
Vulnerable code example: Command Injection
This code is intentionally vulnerable for testing purposes.
"""

import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    
    # VULNERABLE: Command Injection
    result = os.system(f"ping -c 4 {host}")
    return f"Ping result: {result}"

@app.route('/execute')
def execute():
    cmd = request.args.get('cmd')
    
    # VULNERABLE: Command Injection via subprocess
    output = subprocess.check_output(cmd, shell=True)
    return output

@app.route('/backup')
def backup():
    filename = request.args.get('file')
    
    # VULNERABLE: Command Injection
    os.system("tar -czf backup.tar.gz " + filename)
    return "Backup created"

@app.route('/convert')
def convert():
    input_file = request.args.get('input')
    output_file = request.args.get('output')
    
    # VULNERABLE: Command Injection
    command = f"convert {input_file} {output_file}"
    subprocess.call(command, shell=True)
    return "Conversion complete"

@app.route('/grep_logs')
def grep_logs():
    search_term = request.args.get('term')
    
    # VULNERABLE: Command Injection
    result = os.popen(f"grep '{search_term}' /var/log/app.log").read()
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

