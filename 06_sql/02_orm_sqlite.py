from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# 初始化应用和数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Role(db.Model):
    """用户权限"""
    id = db.Column('id', db.INTEGER, primary_key=True)  # 设置id为整型主键，默认自增
    role = db.Column('role', db.VARCHAR(100))
    # relationshhip 将Role和User表关联到一起
    # 正向查询：当查询到一个 role 对象时，可以通过 role.modules 查询出该角色的所有用户
    # 反向查询：当查询到一个 user 对象时，可以通过 user.myrole 查询出该用户的角色
    users = db.relationship('User', backref='myrole', lazy='dynamic')

    def __str__(self):
        return f'{self.id} \t {self.role}'


class User(db.Model):
    """用户表"""
    id = db.Column('id', db.INTEGER, primary_key=True)  # 设置id为整型主键，默认自增
    name = db.Column('name', db.VARCHAR(20))
    desc = db.Column('desc', db.VARCHAR(100))
    # foreignkey 关联role表的id字段
    role_id = db.Column('role_id', db.INTEGER, db.ForeignKey("role.id"), nullable=False)

    def __init__(self, name, desc, role_id):
        self.name = name
        self.desc = desc
        self.role_id = role_id

    def __str__(self):
        return f'{self.id} \t {self.name} \t {self.desc} \t '


@app.before_request
def before():
    # 创建所有表
    db.create_all()


@app.teardown_request
def teardown(exception):
    pass


@app.route("/role")
def role():
    role = Role.query.filter_by(id=1).first()
    # 正向查询
    for user in role.users:
        print(user)
    return "role"


@app.route("/")
def index():
    # 查询
    li = User.query.all()  # 以列表形式获取所有结果
    for user in li:
        print(user, user.myrole.role)   # 通过user对象查询角色

    # User.query.filter_by(name='peter').first()
    # User.query.filter(User.desc.endswith('sh')).all()
    # User.query.order_by(User.name.desc()).all()
    # limit限制数量，offset 偏移
    # User.query.limit(10).offset(2).all()
    # User.query.get(1)

    return "index"


@app.route("/insert")
def insert():
    # 创建用户
    admin = User('admin', '管理员', 1)
    guest = User('guest', '访客', 3)
    # 将用户写入数据库
    # db.session.add(admin)
    # db.session.add(guest)
    db.session.add_all([admin, guest])  # 一次性添加多条数据
    db.session.commit()

    return 'insert'


@app.route("/update")
def update():
    user = User.query.filter_by(name='guest').first()
    user.name = 'guest_1'
    db.session.add(user)
    db.session.commit()
    return "update"


@app.route("/del")
def delete():
    # first_or_404 如果不存在，则返回404
    user = User.query.filter_by(name='admin').first_or_404()
    db.session.delete(user)
    db.session.commit()
    return "delete"


if __name__ == "__main__":
    app.run(debug=True)
