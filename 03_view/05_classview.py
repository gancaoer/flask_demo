from flask import Flask, request
from flask.views import View

"""类视图（可插拔视图）"""


app = Flask(__name__)


class MyView(View):
    # 可以使用 methods 来限制请求方法
    methods = ["GET", "POST"]

    # get请求方法的执行逻辑
    def get(self):
        return "test get"

    # post请求方法执行的逻辑
    def post(self):
        return "test post"

    # 调度函数，必须重写。不重写，View类会直接抛异常
    def dispatch_request(self):
        # 请求方法映射关系
        request_method = {"get": self.get(), "post": self.post()}
        # 通过requset方法获取前端访问的请求方法
        print(request.method)
        # 通过请求方法，映射到对应的函数对象
        view = request_method.get(request.method.lower())
        print(view)
        # 返回映射到的函数返回值
        return view


# 只能采用集中注册
# as_view方法将类转成视图函数，参数是最终视图的名称
app.add_url_rule("/myview", view_func=MyView.as_view("myview"))

if __name__ == "__main__":
    app.run(debug=True)