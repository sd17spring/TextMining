"""
Put your Flask app code here.
"""

from flask import Flask
from flask import render_template
from flask import request
import os
app = Flask(__name__)


@app.route('/return',  methods=['POST', 'GET'])
def hello_world():
    print('in method')
    error = None
    if request.method == 'POST':
        if(request.form['Name'] != '' and request.form['Age'] != '' and request.form['Favorite Softdes Ninja'] != ''):
            name = request.form['Name']
            age = request.form['Name']
        else:
            error = 'Input Required'

    #         error = 'Invalid username/password'
    # if request.method == 'GET':
    name = request.form['Name']
    age = request.form['Age']
    print(name)
    print(age)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('return.html', name=name, age=age, error=error)


@app.route('/ajax', methods=['GET'])
def changeConent():
    print('this was accessed')
    return 'This is Ajax Request Respose from the Server. Sent without reloading the page'


@app.route('/')
def hello(name=None):
    return render_template('index.html',name = name)



if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host=HOST, port=PORT)
