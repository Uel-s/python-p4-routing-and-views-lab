#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count_str = ''
    for n in range(number):
        count_str += f'{n}\n'
    return count_str

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Division by zero is not allowed'

    elif operation == '%':
        if num2 != 0:
            return str(num1 % num2)
        else:
            return 'Modulo by zero is not allowed'

    return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555)