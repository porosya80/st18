from flask import Flask

app = Flask(__name__)

@app.route('/test')
def home():
    return 'hello world'




if __name__ == '__main__':
    app.run()