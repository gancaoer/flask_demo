from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

"""自定义路由转换"""

app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, map, regex):
        super().__init__(map)
        # 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        """URL路径中的参数需要先经过该函数处理后再返回（返回值作为参数传递给视图函数）"""
        return str(int(value)+1)

    def to_url(self, value):
        """处理使用URL提交的参数"""
        # 使用url_for反转时，处理传递的参数，返回的值用于生成URL中的参数
        return str(int(value)+5)


# 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter


# 使用自定义的路由转换器，
@app.route(r'/<re(r"1[34578]\d{9}$"):mobile>')
def mobile(mobile):
    return mobile


@app.route('/index/mobile')
def index(mobile='15620200000'):
    return redirect(url_for("mobile", mobile=mobile))


if __name__ == '__main__':
    app.run(debug=True)

