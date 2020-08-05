from flask import Flask, jsonify, send_file, request, session
from flask_cors import CORS
import sys
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

# 分组数据对象类，用于快速映射生成json对象
class group_obj:
    def __init__(self, group_id, group_name, add_datetime, upd_datetime):
        self.group_id = group_id
        self.group_name = group_name
        self.add_datetime = add_datetime
        self.upd_datetime = upd_datetime

# 单词数据对象类，用于快速映射生成json对象
class word_obj:
    def __init__(self, words_id, group_id, words_jp, trans_cn, add_datetime, upd_datetime):
        self.words_id = words_id
        self.group_id = group_id
        self.words_jp = words_jp
        self.trans_cn = trans_cn
        self.add_datetime = add_datetime
        self.upd_datetime = upd_datetime

# 工具类：时间戳转换日期文本
def util_timestamp_2_date(timestamp):
    timeArray = time.localtime(int(timestamp))
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return formatTime

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
            sql = 'insert into "main"."group"("group_id", "group_name", "add_datetime", "upd_datetime") VALUES (NULL, \'' + str(para_json_obj["group_name"]) +'\', ' + str(current_time) +', ' + str(current_time) +')'
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
            return "add_success"

# 获取全部词汇分组
@app.route("/group", methods=['GET'])
def get_group():
    sql = 'SELECT group_id, group_name, add_datetime, upd_datetime FROM "group"'
    conn = sqlite3.connect('data/core.db')
    c = conn.cursor()
    cursor = c.execute(sql)
    data_groups = []
    for row in cursor:
        data_groups.append(json.loads(json.dumps(group_obj(row[0], row[1], util_timestamp_2_date(row[2]), util_timestamp_2_date(row[3])).__dict__, ensure_ascii=True)))
    return json.dumps(data_groups)

# 添加单词
# 参数(json)：
# 1. words_jp (日语单词,必须)
# 2. trans_cn (中文意思,必须)
# 3. group_id (所在分组ID,必须)
@app.route("/word", methods=['POST'])
def add_word():
    if request.get_data(as_text=True) != '':
        para_json_obj = json.loads(request.get_data(as_text=True))
        if ("words_jp" not in para_json_obj or "trans_cn" not in para_json_obj or "group_id" not in para_json_obj):
            return "parameter_missing"
        else:
            current_time = int(time.time())
            sql = 'insert into "main"."words"("words_id", "group_id", "words_jp", "trans_cn", "add_datetime", "upd_datetime") VALUES (NULL, \'' + str(para_json_obj["group_id"]) +'\', \'' + str(para_json_obj["words_jp"]) +'\', \'' + str(para_json_obj["trans_cn"]) + '\', '  + str(current_time) +', ' + str(current_time) +')'
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
            return "add_success"

# 获取全部单词
@app.route("/word", methods=['GET'])
def get_word():
    sql = 'SELECT words_id, group_id, words_jp, trans_cn, add_datetime, upd_datetime FROM "words"'
    conn = sqlite3.connect('data/core.db')
    c = conn.cursor()
    cursor = c.execute(sql)
    data_words = []
    for row in cursor:
        data_words.append(json.loads(json.dumps(word_obj(row[0], row[1], row[2], row[3], util_timestamp_2_date(row[4]), util_timestamp_2_date(row[5])).__dict__, ensure_ascii=True)))
    return json.dumps(data_words)

# 删除单词
# 参数(json)：
# 1. words_id (单词ID,必须)
@app.route("/word", methods=['DELETE'])
def del_word():
    if request.get_data(as_text=True) != '':
        para_json_obj = json.loads(request.get_data(as_text=True))
        if ("words_id" not in para_json_obj):
            return "parameter_missing"
        else:
            sql = 'DELETE FROM "words" WHERE words_id = '+str(para_json_obj["words_id"])
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            try:
                cursor = c.execute(sql)
                conn.commit()
                if conn.total_changes != 0:
                    return "del_success"
                else:
                    return "del_error"
            except:
                return "del error:" + sys.exc_info()[0]
            finally:
                conn.close()
            

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    PORT = int(os.getenv('PORT', 8000))
    HOST = str(os.getenv('host', '0.0.0.0'))

    app.run(host=HOST, port=PORT)