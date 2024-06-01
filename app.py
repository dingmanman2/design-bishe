from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query,get_KGQA_answer,get_answer_profile
from KGQA.ltp import get_target_array
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
#路由匹配url中的acton

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index(name=None):
    return render_template('index.html', name = name)


#返回搜索页面模板 search.html
@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

#返回问答页面模板 KGQA.html
@app.route('/KGQA', methods=['GET', 'POST'])
def KGQA():
    return render_template('KGQA.html')
#前端传递的人物名称参数，调用 get_answer_profile 函数获取人物资料和头像，并返回 JSON 格式的数据。
@app.route('/get_profile',methods=['GET','POST'])
def get_profile():
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)
    return jsonify(json_data)
#根据前端传递的问题参数，调用 get_KGQA_answer 函数获取问题的答案和相关人物资料，并返回 JSON 格式的数据。
@app.route('/KGQA_answer', methods=['GET', 'POST'])
def KGQA_answer():
    question = request.args.get('name')
    json_data = get_KGQA_answer(get_target_array(str(question)))
    return jsonify(json_data)
#根据前端传递的人物名称参数，调用 query 函数查询知识图谱中与该人物相关的信息，并返回 JSON 格式的数据
@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data=query(str(name))
    return jsonify(json_data)
#：返回所有人物关系页面模板 all_relation.html。
@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')
#启动服务器
if __name__ == '__main__':
    app.run(debug=True)
#render_template 函数用于渲染模板，
# request.args.get 函数用于获取前端传递的参数，
# jsonify 函数用于将数据转换为 JSON 格式，以便前端处理。