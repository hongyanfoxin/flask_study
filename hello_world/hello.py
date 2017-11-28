from flask import Flask
app = Flask(__name__)

@app.route("/<int:id>")
def hello(id):
    return "Hello %s!" % id

if __name__ == "__main__":
    app.run()
