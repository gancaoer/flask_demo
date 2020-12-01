from flask import Flask, render_template

app = Flask(__name__)

'''模板简介'''


@app.route("/")
@app.route("/<name>")
def index(name=None):
    return render_template("01.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)
