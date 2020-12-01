from flask import Flask, render_template

app = Flask(__name__)

'''模板继承'''


@app.route("/")
def index():
    return render_template('06_inherit.html')


if __name__ == '__main__':
    app.run(debug=True)
