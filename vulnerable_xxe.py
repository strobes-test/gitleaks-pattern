#!/usr/bin/env python3
"""
Vulnerable code example: XML External Entity (XXE) Injection
This code is intentionally vulnerable for testing purposes.
"""

import xml.etree.ElementTree as ET
from lxml import etree
from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_xml', methods=['POST'])
def parse_xml():
    xml_data = request.data
    
    # VULNERABLE: XXE - ElementTree with default settings
    tree = ET.fromstring(xml_data)
    return f"Parsed: {tree.tag}"

@app.route('/parse_lxml', methods=['POST'])
def parse_lxml():
    xml_data = request.data
    
    # VULNERABLE: XXE - lxml without restrictions
    parser = etree.XMLParser()
    tree = etree.fromstring(xml_data, parser)
    return etree.tostring(tree).decode()

@app.route('/process_xml', methods=['POST'])
def process_xml():
    xml_content = request.data.decode('utf-8')
    
    # VULNERABLE: XXE via XML parsing
    root = ET.fromstring(xml_content)
    data = {}
    for child in root:
        data[child.tag] = child.text
    return str(data)

@app.route('/validate_xml', methods=['POST'])
def validate_xml():
    xml_data = request.data
    
    # VULNERABLE: XXE with DTD processing enabled
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.fromstring(xml_data, parser)
    return "Valid XML"

if __name__ == '__main__':
    app.run(debug=True)

