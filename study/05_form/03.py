import re
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, SubmitField, IntegerField
from wtforms.validators import Length

"""自定义校验器"""


app = Flask(__name__)
app.secret_key = "terre"


class Mobile:
    regex = re.compile(r'^1[35789]\d{9}$')

    def __init__(self, message=None):
        if message is None:
            self.message = "手机号码格式不正确！"
        self.message = message

    def __call__(self, form, field):
        match = self.regex.match(field.data)
        if not match:
            raise ValidationError(self.message)
        return match


# 自定义表单类，需继承Form表单
class MyForm(FlaskForm):
    mobile = StringField('mobile', validators=[Length(min=11, max=11, message='手机号位数不对'),
                                               Mobile(message='手机号格式不对')])
    submit = SubmitField('Register')


@app.route("/", methods=["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        mobile = form.mobile.data
        return mobile
    else:
        msg = form.mobile.errors
        if msg:
            flash(msg[0])
        return render_template("03.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
