from flask import Flask, jsonify, send_file, request, session
from flask_cors import CORS
import json
import os
import ssl as ssl_lib
import certifi
import requests
import sqlite3

app = Flask(__name__, static_folder='static/static')
CORS(app, resources=r'/*')

@app.route("/", methods=['GET'])
def index():
    return send_file('static/index.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    PORT = int(os.getenv('PORT', 8000))
    HOST = str(os.getenv('host', '0.0.0.0'))

    app.run(host=HOST, port=PORT)