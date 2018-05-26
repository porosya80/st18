from flask import Flask, request
import os
import random


SEED = os.environ['FLASK_RANDOM_SEED']

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

random.seed(SEED)


class Dig:
    def __init__(self):
        self.num_to_guess = 5
        self.tries = 0

    def gen(self):
        self.num_to_guess = random.randint(1, 10)

    def compare(self, num):
        if int(num) == self.num_to_guess:
            self.gen()
            return f"YOu win, generating new one, you use {self.tries} tries"
        elif int(num) < self.num_to_guess:
            self.tries +=1
            return "<"
        elif int(num) > self.num_to_guess:
            self.tries +=1
            return ">"


thisone=Dig()


@app.route('/', methods=['GET'])
def number_gen():
    thisone.gen()
    return f'ok.just guess number'


@app.route('/guess/', methods=['POST'])
def number_check():
    print(request.form)
    numb = request.form["num"]
    if thisone.num_to_guess == 0:
        return f'Generate digit for first'
    return f'{thisone.compare(numb)}', f'{thisone.num_to_guess}'


# @app.route('/', methods=['POST'])
# def number_guess():
#     pass


if __name__ == '__main__':
    app.run()