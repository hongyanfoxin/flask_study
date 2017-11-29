from flask import Flask, request, make_response, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from os import path

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files["file"]
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path, 'static\\uploads\\')
        file_name = upload_path + secure_filename(f.filename)
        f.save(file_name)
        return 'successs'

    return render_template("upload.html")


if __name__ == "__main__":
    app.run()
