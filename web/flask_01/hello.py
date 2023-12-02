from flask import Flask, abort
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}! Start to explore the flask framework.</h1>'.format(name)


@app.route('/user/number/<id>')
def get_user(id):
    if int(id) == 0:
        abort(404)
    return "<h1>Hello, {}</h1>".format(id)


@app.route('/user_agent')
def get_user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@app.route("/redirect")
def go_to_web():
    return redirect("https://www.baidu.com")


if __name__ == '__main__':
    app.run(debug=True)
