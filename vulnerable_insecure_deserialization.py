#!/usr/bin/env python3
"""
Vulnerable code example: Insecure Deserialization
This code is intentionally vulnerable for testing purposes.
"""

import pickle
import yaml
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_pickle', methods=['POST'])
def load_pickle():
    data = request.data
    
    # VULNERABLE: Insecure Deserialization with pickle
    obj = pickle.loads(data)
    return str(obj)

@app.route('/load_yaml', methods=['POST'])
def load_yaml():
    yaml_data = request.data.decode('utf-8')
    
    # VULNERABLE: Unsafe YAML loading
    obj = yaml.load(yaml_data)
    return str(obj)

@app.route('/deserialize_object')
def deserialize_object():
    serialized = request.args.get('data')
    
    # VULNERABLE: Pickle deserialization from user input
    import base64
    decoded = base64.b64decode(serialized)
    obj = pickle.loads(decoded)
    return f"Object loaded: {obj}"

@app.route('/load_config', methods=['POST'])
def load_config():
    config_data = request.get_json()
    
    # VULNERABLE: eval() with user input
    result = eval(config_data.get('expression'))
    return str(result)

@app.route('/execute_code', methods=['POST'])
def execute_code():
    code = request.form.get('code')
    
    # VULNERABLE: exec() with user input
    exec(code)
    return "Code executed"

if __name__ == '__main__':
    app.run(debug=True)

