from flask import Flask, render_template
import time

app = Flask(__name__)

'''宏与全局函数'''


# 自定义全局函数
# @app.template_global('current_time')
def current_time(timeFormat="%Y-%m-%d %H:%M:%S"):
    return time.strftime(timeFormat)

# 也可以使用 add_template_global
app.add_template_global(current_time, 'current_time')


@app.route("/")
def index():
    list_dict = [{"name": "zhangsan", "sex": "男", "age": 22},
                 {"name": "lisi", "sex": "女", "age": 18},
                 {"name": "wangwu", "sex": "男", "age": 56}]
    return render_template("05_macro.html", list_dict=list_dict)


if __name__ == '__main__':
    app.run(debug=True)
