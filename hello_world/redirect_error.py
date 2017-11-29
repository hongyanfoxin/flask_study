from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    # this_is_never_executed()


@app.errorhandler(401)
def unauthorized(error):
    # this type is unicode
    # print(type(render_template('errorhandler_401.html')))
    return render_template('errorhandler_401.html'), 401


if __name__ == "__main__":
    app.run()
