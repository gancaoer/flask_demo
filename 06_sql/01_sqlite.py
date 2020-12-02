import sqlite3
from flask import g, Flask, request, render_template, redirect, url_for


"""原始方式操作sqlite"""


app = Flask(__name__)
DATABASE = '01_sqlite.db'


# 连接数据库
def connect_db():
    db = sqlite3.connect(DATABASE)
    g.db = db
    g.c = db.cursor()


# 初始化
@app.before_request
def before_request():
    connect_db()
    # 创建表
    sql = '''create table if not exists user(id integer primary key autoincrement not null , 
        name char(50) not null, 
        desc char(500))'''
    g.c.execute(sql)
    g.db.commit()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route("/", methods=['POST', 'GET'])
def index():
    q = '''select * from user'''
    g.c.execute(q)
    li = g.c.fetchall()  # 获取结果集的所有行
    return render_template("01_index.html", li=li)


@app.route("/insert", methods=['POST', "GET"])
def insert():
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data.get("name")
        desc = data.get("desc")
        q = f'''insert into user(name, desc) values("{name}", "{desc}")'''
        g.c.execute(q)
        g.db.commit()
        return redirect(url_for("index"))
    return render_template("01_insert.html")


if __name__ == "__main__":
    app.run(debug=True)