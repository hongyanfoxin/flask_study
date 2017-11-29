from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# @app.route('/hello/')
# @app.route("/hello/<name>")
# def hello(name=None):
#     return render_template('hello.html', name=name)

@app.route("/hello/<name>")
def hello(name=None):
    return request.args.get('user', '')

if __name__ == "__main__":
    app.run()
