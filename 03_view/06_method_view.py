from flask import Flask
from flask.views import MethodView

"""类视图（可插拔视图）"""


app = Flask(__name__)


class MyView(MethodView):
    # 可以使用 methods 来限制请求方法
    methods = ["GET", "POST"]

    # get请求方法的执行逻辑
    def get(self):
        return "test get"

    # post请求方法执行的逻辑
    def post(self):
        return "test post"


# 只能采用集中注册
# as_view方法将类转成视图函数，参数是最终视图的名称
app.add_url_rule("/myview", view_func=MyView.as_view("myview"))

if __name__ == "__main__":
    app.run(debug=True)