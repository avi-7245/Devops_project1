from flask import Flask

app = Flask(__name__)

@app.route("/info")
def myinfo():
    return "my name is sonu raj."

@app.route("/phone")
def myphone():
    return "7050511191"

app.run(host="0.0.0.0")
