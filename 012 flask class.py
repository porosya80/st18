from flask import Flask

app = Flask(__name__)


@app.route('/<user>')
def home(user):
    return f'hello world, {user}'


@app.route('/second/<first>/<second>')
def home2(first, second):
    return f'this is second task and result is {int(first) + int(second)}'

@app.route('/third/<first>/<second>/<third>')
def home3(first, second, third):
    return f'this is second task and result is {max(first,second,third,key = len)}'


if __name__ == '__main__':
    app.run()
