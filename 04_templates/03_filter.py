from flask import Flask, render_template

app = Flask(__name__)

'''过滤器'''


# 自定义过滤器
def filter_double_sort(li):
    return li[::2]


# 方式一：使用 add_templage_filter函数
# 在模板中使用过滤器的名字即可，若未指定则为函数名，如 {{ [3,9,1,7] | double_2 }}
app.add_template_filter(filter_double_sort, 'double_2')


# 方式二：使用 app.template_filter 装饰器
@app.template_filter('sub')
def sub(li, start, end):
    return li[start:end]


@app.route("/")
def index():
    list_dict = [{"name": "zhangsan", "sex": "男", "age": 22},
                 {"name": "lisi", "sex": "女", "age": 18},
                 {"name": "wangwu", "sex": "男", "age": 56}]
    return render_template("03_filter.html", list_dict=list_dict)


if __name__ == '__main__':
    app.run(debug=True)
