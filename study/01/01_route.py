from flask import Flask, current_app, request

# 1. 创建flask的应用对象
app = Flask(__name__,  # 应用程序包名，__name__表示当前模块的名称，flask将以这个模块所在的目录为总目录，默认这个目录中的static为静态文件夹
            static_url_path="../day01/static",  # 访问静态资源的URL前缀，默认为static_folder中指定的文件夹
            static_folder="static",  # 静态文件的目录，默认 static
            template_folder="templates")    # 模板文件的目录，默认 templates
# static_url_path：若指定 static_url_path为 /path，则访问 http://127.0.0.1/path/login.html 表示访问静态文件夹中的 login.html文件

# 配置参数
# （1）使用配置文件配置参数
# app.config.from_pyfile("config.cfg")

# （2）使用对象配置参数
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)

# (3) 直接操作config的字典对象
app.config["DEBUG"] = True


@app.route('/')     # route()函数，告诉应用程序哪个URL应该调用相关的函数
def hello_world():
    """定义的视图函数"""

    # 在视图中读取配置参数
    # (1)从全局对象app的config中取值
    print(app.config.get("DEBUG"))
    # （2）通过current_app获取
    # print(current_app.config.get("DEBUG"))
    return 'Hello World1!'

# app.add_url_rule() 集中注册机制


if __name__ == '__main__':
    # 启动 flask 程序
    # host 要监听的主机名，默认127.0.0.1
    # port 监听的端口号，默认5000
    # debug 提供调试信息，若为True，修改代码后服务器会自动重新加载
    app.run()

