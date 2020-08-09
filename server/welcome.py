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

# 考试结果对象类，用于快速映射生成json对象
class exam_result_obj:
    def __init__(self, test_id, score, finish_datetime):
        self.test_id = test_id
        self.score = score
        self.finish_datetime = finish_datetime

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
@app.route("/api/group", methods=['POST'])
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
@app.route("/api/group", methods=['GET'])
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
@app.route("/api/word", methods=['POST'])
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
@app.route("/api/word", methods=['GET'])
def get_word():
    sql = 'SELECT words_id, group_id, words_jp, trans_cn, add_datetime, upd_datetime FROM "words" order by upd_datetime DESC'
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
@app.route("/api/word", methods=['DELETE'])
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
                return "del error:" + str(sys.exc_info()[0])
            finally:
                conn.close()
            
# 创建考试
# 参数(get url)：
# 1. words_group (单词分组,必须)
# 2. type (考试种类,必须,汉译日-1；日译汉-2)
@app.route("/api/exam", methods=['GET'])
def create_exam():
    group = request.args.get("words_group")
    exam_type = request.args.get("type")
    # 为空或缺少参数判断
    if group == None or exam_type == None or group == '' or exam_type == '':
        return "parameter_error"
    # 考试种类判断
    if exam_type != '1' and exam_type != '2':
        return "exam_type_error"
    conn = sqlite3.connect('data/core.db')
    c = conn.cursor()
    # 单词分组判断
    sql_group_exist = 'SELECT group_id FROM "group" WHERE group_id= '+str(group)
    cursor = c.execute(sql_group_exist)
    list_group_exist = cursor.fetchall()
    if len(list_group_exist) > 0:
        # 从词汇表中根据指定单词分组随机抽取20条数据（若不足20条则返回随机乱序的全部记录）
        sql_get_words = 'SELECT words_id, group_id, words_jp, trans_cn, add_datetime, upd_datetime FROM words WHERE group_id= '+ str(group) +' ORDER BY RANDOM() limit 20;'
        cursor = c.execute(sql_get_words)
        list_exam_words = cursor.fetchall()
        if len(list_exam_words) > 0:
            record_id = 1
            # 创建考试ID，使用当前时间戳作为考试ID
            exam_id = int(time.time())
            # 将考试ID和词汇列表封装，用于返回给前台
            data_words = []
            for row in list_exam_words:
                data_words.append(json.loads(json.dumps(word_obj(row[0], row[1], row[2], row[3], util_timestamp_2_date(row[4]), util_timestamp_2_date(row[5])).__dict__, ensure_ascii=True)))
                # 将随机抽取的词汇ID和其他考试信息写入到考试记录表中
                sql_test_record = 'INSERT INTO test_record (test_id, record_id, "type", words_id, answer, add_datetime, ans_datetime) VALUES('
                sql_test_record = sql_test_record + str(exam_id) + ', '
                sql_test_record = sql_test_record + str(record_id) + ', '
                sql_test_record = sql_test_record + str(exam_type) + ', '
                sql_test_record = sql_test_record + str(row[0]) + ', '
                sql_test_record = sql_test_record + 'NULL' + ', '
                sql_test_record = sql_test_record + str(exam_id) + ', '
                sql_test_record = sql_test_record + 'NULL' + ')'
                c.execute(sql_test_record)     
                record_id += 1
            conn.commit()
            conn.close()
            exam_detail_info = {}
            exam_detail_info['exam_id'] = exam_id
            exam_detail_info['exam_words'] = data_words
            return json.dumps(exam_detail_info)
        else:
            # 当前分组下没有词汇
            conn.close()
            return "group_has_no_words"
    else:
        # 词汇分组不存在
        conn.close()
        return "words_group_error"

# 提交小题
# 参数(json)
# 1. test_id (考试ID,必须)
# 2. words_id (单词ID，必须)
# 3. answer (答案，必须)
@app.route("/api/exam", methods=['POST'])
def upd_answer():
    if request.get_data(as_text=True) != '':
        para_json_obj = json.loads(request.get_data(as_text=True))
        if ("test_id" not in para_json_obj or "words_id" not in para_json_obj or "answer" not in para_json_obj):
            return "parameter_missing"
        else:
            ans_time = int(time.time())
            sql_upd = 'UPDATE "main"."test_record" SET "answer" = \'' + str(para_json_obj["answer"]) + '\', "ans_datetime" = '+ str(ans_time) +' WHERE "test_id" = '+ str(para_json_obj["test_id"]) +' AND "words_id" = '+ str(para_json_obj["words_id"])
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            try:
                cursor = c.execute(sql_upd)
                conn.commit()
                if conn.total_changes != 0:
                    return "ans_success"
                else:
                    return "ans_error"
            except:
                return "ans error:" + str(sys.exc_info()[0])
            finally:
                conn.close()

# 提交考试，打分记录成绩
# 参数(json)
# 1. test_id (考试ID,必须)
@app.route("/api/exam_result", methods=['POST'])
def com_exam():
    if request.get_data(as_text=True) != '':
        para_json_obj = json.loads(request.get_data(as_text=True))
        if ("test_id" not in para_json_obj):
            return "parameter_missing"
        else:
            com_time = int(time.time())
            sql_get_points = 'SELECT (tr.answer = w.words_jp)*5 AS points FROM "test_record" tr INNER JOIN "words" w ON tr.words_id = w.words_id WHERE tr.test_id = '+ str(para_json_obj["test_id"])
            conn = sqlite3.connect('data/core.db')
            c = conn.cursor()
            try:
                cursor = c.execute(sql_get_points)
                list_points = cursor.fetchall()
                total_points = 0
                if len(list_points) > 0:
                    for row in list_points:
                        total_points = total_points + int(row[0])
                    sql_ins_test_result = 'INSERT INTO "main"."test_result"("test_id", "score", "finish_datetime") VALUES ('+ str(para_json_obj["test_id"]) +', '+ str(total_points) +', '+ str(com_time) +')'
                    cursor = c.execute(sql_ins_test_result)
                    conn.commit()
                    if conn.total_changes != 0:
                        return json.dumps(exam_result_obj(str(para_json_obj["test_id"]), total_points, util_timestamp_2_date(com_time)).__dict__, ensure_ascii=True)
                    else:
                        return "write result error"
                else:
                    return "test_id_incorrect"
            except:
                return "get result error:" + str(sys.exc_info()[0])
            finally:
                conn.close()

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    PORT = int(os.getenv('PORT', 8000))
    HOST = str(os.getenv('host', '0.0.0.0'))

    app.run(host=HOST, port=PORT)