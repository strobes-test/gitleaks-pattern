#!/usr/bin/env python3
"""
Vulnerable code example: Cross-Site Scripting (XSS)
This code is intentionally vulnerable for testing purposes.
"""

from flask import Flask, request, render_template_string, make_response
import html

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    
    # VULNERABLE: XSS - Unescaped user input
    template = "<h1>Hello, " + name + "!</h1>"
    return render_template_string(template)

@app.route('/comment', methods=['POST'])
def post_comment():
    comment = request.form.get('comment')
    
    # VULNERABLE: Reflected XSS
    html_response = f"""
    <html>
        <body>
            <h2>Your comment:</h2>
            <div>{comment}</div>
        </body>
    </html>
    """
    return html_response

@app.route('/search_results')
def search_results():
    query = request.args.get('q', '')
    
    # VULNERABLE: XSS in search results
    response = make_response(f"<html><body><h1>Search results for: {query}</h1></body></html>")
    return response

@app.route('/profile/<username>')
def profile(username):
    # VULNERABLE: XSS via URL parameter
    return f"<h1>Profile of {username}</h1><p>User data goes here</p>"

@app.route('/display_html')
def display_html():
    user_html = request.args.get('content', '')
    
    # VULNERABLE: Directly rendering user-provided HTML
    return render_template_string(user_html)

if __name__ == '__main__':
    app.run(debug=True)

