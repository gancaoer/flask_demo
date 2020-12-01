import json

from flask import Flask, jsonify, make_response


"""请求响应"""

app = Flask(__name__)


@app.route("/1/")
def index():
    data = {"name": "张三", "age": 18}

    # 以元组方式返回响应信息，括号可省略
    # 响应信息（字符串或json），状态码（数字或状态码字符串），响应头（列表或字典）

    # 1. 直接返回
    # return "login", 200, [("name", "admin")]
    # 使用json.dumps时需要加上 ensure_ascii=False，防止中文乱码
    return json.dumps(data, ensure_ascii=False), "888 test", {"name": "admin", "Content-Type": "Application/json"}


@app.route("/2/")
def home():
    # 2. 使用make_response构造响应信息
    resp = make_response({"name": "张三", "age": 18})
    resp.status = "200 OK"
    resp.headers["name"] = "admin"
    return resp


@app.route("/3/")
def login():
    data = {"name": "张三", "age": 18}

    # 3. 使用jsonify
    # jsonify可以将字典转为json数据，并自动设置响应头 content-type为application/json
    # return jsonify(data), 200
    return jsonify(name="张三", age=18), 200  # jsonify也可以直接传入关键字参数


if __name__ == "__main__":
    # 使用 make_response或者jsonify时需要添加此配置确保中文正常输出
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
