from flask import Flask
from flask import render_template
from flask import request
from flask_uwsgi_websocket import GeventWebSocket
import read_lyrics
app = Flask(__name__)
# ws = GeventWebSocket(app)


@app.route('/return',  methods=['POST', 'GET'])
def hello_world():
    print('in method')
    error = None
    body = None
    rr = None
    if request.method == 'POST':
        if(request.form['url'] != ''):
            url = request.form['url']
            rr, body = read_lyrics.rhyme_finder(url)
        else:
            error = 'Input Required'

    #         error = 'Invalid username/password'
    # if request.method == 'GET':
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('return.html', rr='<span style="background-color: #0000FF">test</span>', body=body, error=error)

@app.route('/')
def start_temp():
    return render_template('index.html')


@app.route('/nextWord', methods=['POST'])
def changeConent():



# @ws.route('/websocket')
# def audio(ws):
#     print("got in def audio")
#     first_message = True
#     total_msg = ""
#     sample_rate = 0
#
#     while True:
#         msg = ws.receive()
#
#         if first_message and msg is not None: # the first message should be the sample rate
#             # sample_rapte = getSampleRate(msg)
#             # first_message = False
#             print("got first message")
#             continue
#         elif msg is not None:
#             print("get messaeg")
#             # audio_as_int_array = numpy.frombuffer(msg, 'i2')
#             # doSomething(audio_as_int_array)
#         else:
#             break


if __name__ == '__main__':
    app.run(debug = True)
