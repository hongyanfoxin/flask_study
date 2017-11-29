from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('d:\\uploaded_file.txt')
        return 'success'

    return render_template('upload_file.html')


if __name__ == "__main__":
    app.run()
