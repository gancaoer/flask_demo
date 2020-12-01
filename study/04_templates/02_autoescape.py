from flask import Flask, render_template, Markup

app = Flask(__name__)

'''自动转义'''

@app.route("/")
def index():
    name = "<em>姓名</em>"
    sex = "<em>性别</em>"
    age = "<em>年龄</em>"
    place = "<em>地区</em>"

    # 关闭自动转义推荐使用 Markup
    age = Markup(age)

    return render_template("02_autoescape.html", name=name, sex=sex, age=age, place=place)


if __name__ == '__main__':
    app.run(debug=True)
