from flask import Flask, url_for

app = Flask(__name__)

"""路由参数默认值"""


# 分别访问 127.0.0.1:5000/index/ 和 127.0.0.1:5000/index/test 查看结果
@app.route("/index")
@app.route("/index/<name>")
def index(name='admin'):    # 使用函数形参设置默认值
    return name


# 访问 127.0.0.1:5000/home 查看结果
# defaults默认参数设置，必须在视图函数中定义一个形参来接收
@app.route("/home", defaults={"name": "admin"})
def home(name):
    return name


if __name__ == '__main__':
    app.run(debug=True)


