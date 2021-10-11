
from flask import Flask
from random import uniform

app = Flask(__name__)

@app.route('/<int:num>/')
def number(num):
    return str(num - 1) + ' < ' + str(num) + ' < ' + str(num + 1)

@app.route('/-<int:num>/')
def negativenumber(num):
    return number(-num)

@app.route('/-<float:num1>+<float:num2>/')
@app.route('/-<float:num1>+<int:num2>/')
@app.route('/-<int:num1>+<float:num2>/')
@app.route('/-<int:num1>+<int:num2>/')
def negativesum(num1, num2):
    return sum(-num1, num2)

@app.route('/-<float:num1>-<float:num2>/')
@app.route('/-<float:num1>-<int:num2>/')
@app.route('/-<int:num1>-<float:num2>/')
@app.route('/-<int:num1>-<int:num2>/')
def negativedif(num1, num2):
    return dif(-num1, num2)

@app.route('/<float:num1>+<float:num2>/')
@app.route('/<float:num1>+<int:num2>/')
@app.route('/<int:num1>+<float:num2>/')
@app.route('/<int:num1>+<int:num2>/')
@app.route('/<num1>+<num2>/')
def sum(num1, num2):
    return str(num1 + num2)

@app.route('/<float:num1>-<float:num2>/')
@app.route('/<float:num1>-<int:num2>/')
@app.route('/<int:num1>-<float:num2>/')
@app.route('/<int:num1>-<int:num2>/')
def dif(num1, num2):
    return str(num1 - num2)

@app.route('/randomPI<int:num>')
def randomPI(num):
    hits = 0
    for i in range (0, num):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if (x * x + y * y <= 1): 
            hits += 1
    return str(hits / num * 4)


@app.route('/')
def index():
    return 'Helloworld'

if __name__ == "__main__":
    app.run()