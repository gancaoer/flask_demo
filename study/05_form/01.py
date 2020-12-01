# 导入wtf扩展提供的表单及验证器
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, DateField, IntegerField, \
    DecimalField, SelectMultipleField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, NumberRange
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "terre"


# 自定义表单类，需继承Form表单
class MyForm(FlaskForm):
    # 字段名最好与表中中的name属性、数据库里面的字段名一致
    # label设置标签名
    # validators 验证
    # Text Field类型，文本输入框，必填，用户名长度为4到25之间
    username = StringField('Username', validators=[Length(min=4, max=25)])

    # Text Field类型，文本输入框，Email格式，邮件格式校验需要安装 email-validator
    email = StringField('Email Address', validators=[Email()])

    # Text Field类型，密码输入框，必填，必须同confirm字段一致
    password = PasswordField('Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])

    # Text Field类型，密码输入框
    confirm = PasswordField('Repeat Password')

    # Text Field类型，文本输入框，必须输入整型数值，范围在16到70之间
    age = IntegerField('Age', validators=[NumberRange(min=16, max=70)])

    # Text Field类型，文本输入框，必须输入数值，显示时保留一位小数
    height = DecimalField('Height (Centimeter)', places=1)

    # Text Field类型，文本输入框，必须输入是"年-月-日"格式的日期
    birthday = DateField('Birthday', format='%Y-%m-%d')

    # Radio Box类型，单选框，choices里的内容会在ul标签里，里面每个项是(值，显示名)对
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female')], validators=[DataRequired()])

    # Select类型，下拉单选框，choices里的内容会在Option里，里面每个项是(值，显示名)对
    job = SelectField('Job', choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')
    ])

    # Select类型，多选框，choices里的内容会在Option里，里面每个项是(值，显示名)对
    hobby = SelectMultipleField('Hobby', choices=[
        ('swim', 'Swimming'),
        ('skate', 'Skating'),
        ('hike', 'Hiking')
    ])

    # Text Area类型，段落输入框
    description = TextAreaField('Introduction of yourself')

    # Checkbox类型，加上default='checked'即默认是选上的
    accept_terms = BooleanField('I accept the Terms of Use', default='checked',
                                validators=[DataRequired()])

    # Submit按钮
    submit = SubmitField('Register')


@app.route("/", methods=["POST", "GET"])
def login():
    # 创建表单，Form 是一个带有 CSRF 保护的并且会话安全的表单，若想要禁用csrf保护，可以使用 Form(csrf_enabled=False)
    form = MyForm()

    # 验证表单
    # 使用validate_on_submit来检查是否是一个POST请求并且请求是否验证通过
    '''验证失败的问题
    1. validators 中一定要有 DataRequired()
    2. label 中中文的话需要加Unicode
    3. 表单里没有写 {{ form.csrf_token }}
    4. 表单 method需要指定为 post
    '''
    if form.validate_on_submit():
        name = form.name.data   # 提取前端输入的name的值
        return redirect(url_for("success", name=name))
    else:
        filename = None
        return render_template("01.html", form=form, filename=filename)


@app.route("/success/<name>")
def success(name):
    return f"<h1>欢迎您，{name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
