from flask import Flask

# 1. 创建flask的应用对象
app = Flask(__name__,  # 应用程序包名，__name__表示当前模块的名称，flask将以这个模块所在的目录为总目录，默认这个目录中的static为静态文件夹
            static_url_path="../day01/static",  # 访问静态资源的URL前缀，默认为static_folder中指定的文件夹
            static_folder="static",  # 静态文件的目录，默认 static
            template_folder="templates")    # 模板文件的目录，默认 templates
# static_url_path：若指定 static_url_path为 /path，则访问 http://127.0.0.1/path/login.html 表示访问静态文件夹中的 login.html文件


@app.route('/')
def hello_world():
    """定义的视图函数"""
    return 'Hello World1!'


if __name__ == '__main__':
    app.run(debug=True)

