from flask import Flask, render_template

app = Flask(__name__)

'''测试器'''


# 自定义测试
def start_with(str, suffix):
    return str.lower().startswith(suffix.lower())


# 方式一：使用 add_templage_test函数
# 在模板中使用测试器的名字即可，若未指定则为函数名
app.add_template_test(start_with, 'start_with')


# 方式二：使用 app.template_test 装饰器
@app.template_test('end_with')
def end_with(str, suffix):
    return str.lower().endswith(suffix.lower())


@app.route("/")
def index():
    person = {'name': '张三', 'age': 18}
    return render_template("04_test.html", person=person)


if __name__ == '__main__':
    app.run(debug=True)
