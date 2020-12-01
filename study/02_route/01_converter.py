from flask import Flask, url_for

app = Flask(__name__)

"""路由转换、URL构建"""


# 字符串，缺省值，接收任何不包含斜杠的文本，示例：浏览器访问 http://127.0.0.1:5000/str/zhangsan
@app.route('/str/<username>')
def converter_str(username):
    return f'{username}'


# int，正整数，示例：浏览器访问 http://127.0.0.1:5000/int/46161314
@app.route('/int/<int:order_id>')
def converter_int(order_id):
    return f'{order_id}'


# float，正浮点数，示例：浏览器访问 http://127.0.0.1:5000/float/25.99
@app.route('/float/<float:price>')
def converter_float(price):
    return f'{price}'


# path：类似string，但是可以包含斜杠，示例：浏览器访问 http://127.0.0.1:5000/path/order/515465413
@app.route('/path/<path:url>')
def converter_path(url):
    return f'{url}'


# uuid：接收UUID字符串，示例：浏览器访问 http://127.0.0.1:5000/uuid/85698745-5865-9351-0123-023457189634
@app.route('/uuid/<uuid:user_uuid>')
def converter_uuid(user_uuid):
    return f'{user_uuid}'


if __name__ == '__main__':
    print(app.url_map)  # url_map 查看整个flask的所有路由信息

    # url构建，url_for()使用视图函数的名字找到视图对应的url路径
    with app.test_request_context():
        print('url构建', url_for('converter_str', username="test"))

    app.run(debug=True)


