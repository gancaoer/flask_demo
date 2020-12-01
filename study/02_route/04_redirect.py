from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'home'


@app.route('/login/<username>')
def login(username):
    if username == 'admin':
        return redirect(url_for('way1'))
    return redirect(url_for('home'))  # 重定向，尝试在登录失败时再次显示登陆页面
    # abort(401)    # 如果不想重定向到登录页面，可以使用abort返回错误信息页面


@app.route('/success', endpoint="way1")
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
