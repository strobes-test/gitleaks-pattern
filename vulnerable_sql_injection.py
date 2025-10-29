#!/usr/bin/env python3
"""
Vulnerable code example: SQL Injection
This code is intentionally vulnerable for testing purposes.
"""

import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # VULNERABLE: SQL Injection - String concatenation
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login successful"
    else:
        return "Login failed"

@app.route('/search')
def search():
    search_term = request.args.get('q')
    
    # VULNERABLE: SQL Injection
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{search_term}%'")
    results = cursor.fetchall()
    conn.close()
    
    return str(results)

@app.route('/user/<user_id>')
def get_user(user_id):
    # VULNERABLE: SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    user = cursor.fetchone()
    conn.close()
    
    return str(user)

if __name__ == '__main__':
    app.run(debug=True)

