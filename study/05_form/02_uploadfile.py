from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = "terre"

'''文件上传'''


class MyForm(FlaskForm):
    # 上传文件，可以使用 FileRequired 和 FileAllowed 验证文件上传
    photo = FileField(label=u'头像', validators=[FileRequired(u'头像不能为空'),
                                               FileAllowed(['jpg', 'png', 'gif'], u'请上传图片')])
    submit = SubmitField(label=u'提交')


@app.route("/", methods=["POST", "GET"])
def login():
    form = MyForm()

    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        print(filename)
        # 将上传的文件保存到本地文件中
        form.photo.data.save('d:\\' + filename)

        return '文件上传成功~'
    else:
        filename = None
        msg = form.photo.errors
        if msg:
            flash(msg[0])   # 消息闪现
        return render_template("02_uploadfile.html", form=form, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)


#
# 习题：文件上传
# 限制文件的大小：app.config[“MAX_CONTENT__LENGTH”] = 10*1024*1024
# 让文件可以访问：视图函数中return send_from_directory(os.getcwd(), filename)
# allow_format(file.filename)
# 使用文件原来的名字，需要使用secure_filename()，如file.save(path+secure_filename(file.filename))
# 限制文件格式：不能上传HTML文件，可能引起XSS问题