from flask import Flask

app = Flask(__name__)


# 接收一个get请求，http://127.0.0.1:5000/hello
@app.route('/hello')    # 路由，将URL "/hello" 绑定到hello_world函数
def hello_world():
    return 'Hello World'


# 以上 @app.route("/hello") 也可以使用 add_url_rule
# app.add_url_rule('/hello', 'hello_world', hello_world)


# methods 接收一个post请求，http://127.0.0.1:5000/
@app.route('/', methods=['POST'])   # 默认情况下，flask路由响应 get 请求，可通过methods参数更改此首选项
def index():
    return 'index'


# redirect_to 永久重定向
@app.route("/login", redirect_to="/hello")
def login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=True)
