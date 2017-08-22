from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    for p in request.args:
        print(p, request.args[p])
    return 'I got: a=' + request.args['a']

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
