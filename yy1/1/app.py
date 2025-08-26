import json
import os
from flask import Flask, jsonify, render_template, request
from search_logic import search_schools

# 导入配置
from config import Config

# 获取当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 加载现有JSON数据文件
qq_file_path = os.path.join(base_dir, 'qq.json')
with open(qq_file_path, 'r', encoding='utf-8') as f:
    qq_data = json.load(f)
    # 处理NaN值
    for item in qq_data:
        for key, value in item.items():
            if isinstance(value, float) and value != value:  # 检查是否为NaN
                item[key] = None

pp_file_path = os.path.join(base_dir, 'pp.json')
with open(pp_file_path, 'r', encoding='utf-8') as f:
    pp_data = json.load(f)
    # 处理NaN值
    for item in pp_data:
        for key, value in item.items():
            if isinstance(value, float) and value != value:  # 检查是否为NaN
                item[key] = None

s1_file_path = os.path.join(base_dir, 's1.json')
with open(s1_file_path, 'r', encoding='utf-8') as f:
    s1_data = json.load(f)
    # 处理NaN值
    for item in s1_data:
        for key, value in item.items():
            if isinstance(value, float) and value != value:  # 检查是否为NaN
                item[key] = None

# 检查并加载其他可能的JSON文件
# tt.json
if os.path.exists(os.path.join(base_dir, 'tt.json')):
    with open(os.path.join(base_dir, 'tt.json'), 'r', encoding='utf-8') as f:
        tt_data = json.load(f)
        for item in tt_data:
            for key, value in item.items():
                if isinstance(value, float) and value != value:
                    item[key] = None
else:
    tt_data = []

# t1.json
if os.path.exists(os.path.join(base_dir, 't1.json')):
    with open(os.path.join(base_dir, 't1.json'), 'r', encoding='utf-8') as f:
        t1_data = json.load(f)
        for item in t1_data:
            for key, value in item.items():
                if isinstance(value, float) and value != value:
                    item[key] = None
else:
    t1_data = []

# ttt_database.json
if os.path.exists(os.path.join(base_dir, 'ttt_database.json')):
    with open(os.path.join(base_dir, 'ttt_database.json'), 'r', encoding='utf-8') as f:
        ttt_data = json.load(f)
        for item in ttt_data:
            for key, value in item.items():
                if isinstance(value, float) and value != value:
                    item[key] = None
else:
    ttt_data = []

# gg_database.json
if os.path.exists(os.path.join(base_dir, 'gg_database.json')):
    with open(os.path.join(base_dir, 'gg_database.json'), 'r', encoding='utf-8') as f:
        gg_data = json.load(f)
        for item in gg_data:
            for key, value in item.items():
                if isinstance(value, float) and value != value:
                    item[key] = None
else:
    gg_data = []

# 创建Flask应用
app = Flask(__name__)
app.config.from_object(Config)

# 路由定义
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matches')
def matches():
    return render_template('matches.html')

# API接口：搜索学校
@app.route('/search_schools')
def api_search_schools():
    area = request.args.get('area', '')
    score = request.args.get('score', 0)
    condition = request.args.get('condition', 'regular')
    
    # 调用搜索函数
    results = search_schools(area, score, condition)
    
    return jsonify(results)

# 现有的数据API接口
@app.route('/qq_data')
def get_qq_data():
    return jsonify(qq_data)

@app.route('/pp_data')
def get_pp_data():
    return jsonify(pp_data)

@app.route('/s1_data')
def get_s1_data():
    return jsonify(s1_data)

@app.route('/tt_data')
def get_tt_data():
    return jsonify(tt_data)

@app.route('/t1_data')
def get_t1_data():
    return jsonify(t1_data)

@app.route('/ttt_data')
def get_ttt_data():
    return jsonify(ttt_data)

@app.route('/gg_data')
def get_gg_data():
    return jsonify(gg_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)