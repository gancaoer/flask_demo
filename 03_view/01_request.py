from flask import Flask, request


"""request 请求常用属性之参数"""

app = Flask(__name__)


# 可使用 postman工具模拟发送请求
@app.route("/login", methods=["GET", "POST"])
def login():
    # 获取当前请求方法
    method = request.method.lower()
    if method == "get":
        # request.args 解析url后面带的参数，即get请求的参数
        print(request.args)  # 是ImmutableMultiDict不可变字典
        print(request.args.to_dict())  # 可以使用to_dict()转为普通的可变字典
        print(request.args.get("username"))
    elif method == "post":
        # request.form 获取表单请求数据
        print(request.form)
        print(request.form.to_dict())
        print(request.form.get("username"))

    print("---------------------------------------")
    print('cookie:', request.cookies)
    print('header:', request.headers)
    print("---------------------------------------")
    # values 是form和args，CombinedMultiDict，可以使用values替代form和args
    print('value:', request.values.to_dict())
    # files：通过post或者put请求上传的文件，是MultiDict对象
    print('file:', request.files)
    # data：包含了请求的数据，并转换为字符串
    print('data:', request.data)
    # Json：application / json的数据
    print('json:', request.json)
    print(request.is_json)
    print('get_data:', request.get_data())
    print('get_json:', request.get_json())
    print('environ:', request.environ)
    print('stream:', request.stream)
    return "login"


if __name__ == "__main__":
    app.run(debug=True)