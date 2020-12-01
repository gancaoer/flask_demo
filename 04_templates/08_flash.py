from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'random string'

'''消息闪现'''


@app.route("/")
def index():
    return render_template("08_index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = '密码错误，请重试！'
        else:
            flash("登录成功")
            flash(f"欢迎您{request.form['username']}")
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return render_template("08_login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
