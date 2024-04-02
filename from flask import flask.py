from flask import flask
app=Flask(__name__)
@app.route('/')
def demo():
    return 'i am fine'

@app.route('/lucky/<int:a>/<int:b>')
def lucky(a,b):
    return f'multiple{a},{b}is:{a*b}'
app.run()          