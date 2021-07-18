# Put your app in here.
from flask import Flask, request

app = Flask(__name__)




@app.route('/add')
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{a+b}"

@app.route('/sub')
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{b-a}"

@app.route('/mult')
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{a*b}"

@app.route('/div')
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{a/b}"





# @app.route('/<action>')
# def handle_get(action):
#     a = int(request.args['a'])
#     b = int(request.args['b'])

#     if action == 'add':
#         def add(a, b):
#             """Add a and b."""
#             return a + b

#     elif action == 'sub':
#         def sub(a, b):
#             """Substract b from a."""
#             return a - b

#     elif action == 'mult':
#         def mult(a, b):
#             """Multiply a and b."""
#             return a * b

#     elif action == 'div':
#         def div(a, b):
#             """Divide a by b."""
#             return a / b


