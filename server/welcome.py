from flask import Flask, jsonify, send_file, request, session
from flask_cors import CORS
import json
import os
import ssl as ssl_lib
import certifi
import requests
import sqlite3
import time

app = Flask(__name__, static_folder='static/static')
CORS(app, resources=r'/*')

# Fuck JP Words 后端实现
# 2020-08-04 23:29
# Author: Chita Chou
# env: Python 3.6.5 (Anaconda3 5.2.0) Win x64

@app.route("/", methods=['GET'])
def index():
    return send_file('static/index.html')

# 添加词汇分组
# 参数(json)：
# 1. group_name (分组名称,必须)
@app.route("/group", methods=['POST'])
def add_group():
    if request.get_data(as_text=True) != '':
        para_json_obj = json.loads(request.get_data(as_text=True))
        if ("group_name" not in para_json_obj):
            return "parameter_missing"
        else:
            current_time = int(time.time())
            sql = 'insert into "main"."group"("group_id", "group_name", "add_datetime", "upd_datetime") VALUES (NULL, \''+ para_json_obj["group_name"] +'\', '+ str(current_time) +', '+ str(current_time) +')'
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
            return "add_success"

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    PORT = int(os.getenv('PORT', 8000))
    HOST = str(os.getenv('host', '0.0.0.0'))

    app.run(host=HOST, port=PORT)