from flask import Flask, session, redirect, url_for, request


""" 请求 session """

app = Flask(__name__)

# flask使用session需要设置 secret_key
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'


@app.route('/')
def index():
    if 'username' in session:
        # 获取session
        username = session['username']
        return '登录用户名是:' + username + "<em>，<a href = '/logout'>注销</a><em>"
    return "暂未登录，点击<em><a href = '/login'>登录</a><em>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 设置session
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
    <form action = "" method = "post">
        <p><input type ="text" name ="username"/></p>
        <p><input type ="submit" value ="登录"/></p>
    </form>
    '''


@app.route('/logout')
def logout():
    # 删除指定session
    session.pop("username")
    # session.clear   # 清除所有session
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
