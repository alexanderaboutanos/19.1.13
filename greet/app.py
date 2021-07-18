from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def only_welcome():
        return "welcome"

@app.route('/welcome/<msg>')
def msg_and_welcome(msg=""):
    return f"welcome {msg}"
