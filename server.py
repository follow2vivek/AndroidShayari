from flask import Flask,request,abort
from rivescript import RiveScript
from url import *
from rive import get_reply

app = Flask(__name__)


@app.route(url_alisha,methods = ['POST'])
def parse():
    if request.method == 'POST':
        cmd = request.form['cmd']
        return get_reply(cmd)
    else:
      abort(401)

@app.route(url_index)
def index():
    return "Alisha an Artificial Intelligence"

if __name__ == '__main__':
   app.run(host='0.0.0.0')