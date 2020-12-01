from flask import Flask, make_response, request


"""请求cookie"""

app = Flask(__name__)


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("name", "admin", max_age=3600)   # 设置cookie，默认有效期是临时的，浏览器关闭就失效
    return resp


@app.route("/get_cookies")
def get_cookie():
    my_cookie = request.cookies.get("name")  # 通过request.cookie获取cookie
    return f'{my_cookie}'


@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("admin")  # 删除cookie，只是让cookie过期

    return resp


if __name__ == '__main__':
    app.run(debug=True)