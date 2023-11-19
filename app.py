from flask import Flask,jsonfy


app = Flask(__name__)


@app.route("/")
def index():
    return  "Hello"




app.run(debug=True)