from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/update')
def index():
    with open("log.txt", "a") as f:
        dstr = datetime.datetime.now()
        f.write("%s, " % (dstr))
        f.write("%s, %s,  " % (request.args.get('field1', default=""), request.args.get('field2', default="")))
        f.write("\n");
        r = (%s %s %s)%(dstr, request.args.get('field1', default=""), request.args.get('field2', default=""))
    return 'Thank you -- ' + r
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
