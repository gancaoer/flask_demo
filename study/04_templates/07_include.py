from flask import Flask, render_template

app = Flask(__name__)

'''模板包含'''


@app.route("/")
def index():
    return render_template('07_include.html')


if __name__ == '__main__':
    app.run(debug=True)
