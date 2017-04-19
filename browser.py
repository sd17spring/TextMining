from flask import Flask
from flask import render_template
from flask import request
import read_lyrics
import insertUrl
import os
app = Flask(__name__)
# ws = GeventWebSocket(app)
listColors = ["#00FFFF", "#7FFF00", "#FF8C00","#FF1493", "#FFD700", "#CD5C5C","#FF00FF", "#FFFF00","#00FF7F", "#1E90FF"]


@app.route('/return',  methods=['POST', 'GET'])
def getReturn():
    print('in method')
    error = None
    url = None
    rr = None
    if request.method == 'POST':
        if(request.form['url'] != ''):
            print("into url post")
            url = request.form['url']
            rr, body = read_lyrics.rhyme_finder(url)
            title = read_lyrics.drawOutTitle(url)
            listWords = read_lyrics.drawOutWords(url)
            mydb = insertUrl.databaseConnect("url.db")
            if(mydb.checkVisited(url) is None):
                mydb.creatURLDB(url=url,url2=title,listWords=listWords)
            print(mydb.getWord(title,0))
        else:
            error = 'Input Required'

    #         error = 'Invalid username/password'
    # if request.method == 'GET':
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('return.html', rr = rr, url = url, error=error)

@app.route('/returnFast',  methods=['POST', 'GET'])
def getReturnFast():
    print('in method')
    error = None
    url = None
    rr = None
    if request.method == 'POST':
        if(request.form['url'] != ''):
            print("into url post")
            url = request.form['url']
            rr, body = read_lyrics.rhyme_finder(url)
            title = read_lyrics.drawOutTitle(url)
            listWords = read_lyrics.drawOutWords(url)
            mydb = insertUrl.databaseConnect("url.db")
            if(mydb.checkVisited(url) is None):
                mydb.creatURLDB(url=url,url2=title,listWords=listWords)
            print(mydb.getWord(title,0))
        else:
            error = 'Input Required'

    #         error = 'Invalid username/password'
    # if request.method == 'GET':
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('returnFast.html', rr = rr, url = url, error=error)


@app.route('/')
def start_temp():
    return render_template('index.html')

@app.route('/testReturn',methods=['POST'])
def testReturn():
    print("got in testReturn")
    second = "#00FF00"
    myWord = "myWord"
    last = ";color:#FFFFFF'>" + myWord + " </span>"
    first = "<span style='background-color: " + second + last
    return first

@app.route('/getLength',methods=['POST'])
def getLength():
    if request.method == 'POST':
        print("got in get length")
        if(request.form['url'] != ''):
            url = request.form['url']
            title = read_lyrics.drawOutTitle(url)
            mydb = insertUrl.databaseConnect("url.db")
            count = mydb.getCount(title)
        else:
            error = 'Input Required'
    return str(count)

@app.route('/getNextWord',methods=['POST'])
def getNextWord():
    print("got in getNextWord")
    if request.method == 'POST':
        if(request.form['url'] != '' and request.form['index'] != ''):
            url = request.form['url']
            title = read_lyrics.drawOutTitle(url)
            mydb = insertUrl.databaseConnect("url.db")
            index = int(request.form['index'])
            mainWord = mydb.getWord(title, index)
            textcolor = ";color:#FFFFFF'>"
            usedword = mainWord
            if mydb.checkVisited(url):
                print("correct visited")
                color = mydb.getColor(title,index)
                if(color != 'NA'):
                    textcolor = ";color:#000000'>"
                last = textcolor + mainWord + " </span>"
                first = "<span style='background-color: " + color + last
                if(mainWord == 'NEWLINE'):
                    first = '<br>'
                elif(mainWord == 'BREAKBREAK'):
                    first = '<br><br>'
                return first

            if not read_lyrics.knownWord(mainWord):
                while (not read_lyrics.knownWord(usedword)) and len(usedword) > 1:
                    usedword = usedword[1:len(usedword)]
            if read_lyrics.knownWord(usedword):
                for i in range(1,15):
                    newWord = mydb.getWord(title, index+i)
                    if(newWord == 'BREAKBREAK'):
                        break
                    if not read_lyrics.knownWord(newWord):
                        while (not read_lyrics.knownWord(newWord)) and len(newWord) > 1:
                            newWord = newWord[1:len(newWord)]
                    if(read_lyrics.two_rhyme(usedword, newWord) >= 150):
                        print(mydb.getColor(title, index))
                        if(mydb.getColor(title, index) == 'NA'):
                            mydb.setColor(title, index,listColors[0])
                            mydb.setColor(title, index+i,listColors[0])
                            listColors.append(listColors.pop(0))
                        else:
                            mydb.setColor(title, index+i,mydb.getColor(title, index))
                        # mydb.setColor(title,index-i, "#00FF00")

            # myWord =  mydb.getWord(title, index);
            color = mydb.getColor(title,index)
            if(color != 'NA'):
                textcolor = ";color:#000000'>"
            last =  textcolor + mainWord + " </span>"
            first = "<span style='background-color: " + color + last
            if(mainWord == 'NEWLINE'):
                first = '<br>'
            elif(mainWord == 'BREAKBREAK'):
                first = '<br><br>'
        else:
            first = 'Input Required'
    return first

@app.route('/setVisited',methods=['POST'])
def setVisited():
    if request.method == 'POST':
        if(request.form['url'] != ''):
            url = request.form['url']
            mydb = insertUrl.databaseConnect("url.db")
            mydb.setVisited(url)

@app.route('/getAllWords',methods=['POST'])
def getAllWords():
    finalAdd = ''
    print("got in getAllWords")
    if request.method == 'POST':
        if request.form['url'] != '':
            url = request.form['url']
            title = read_lyrics.drawOutTitle(url)
            mydb = insertUrl.databaseConnect("url.db")
            myWords = mydb.getAllValues(title)
            visited = mydb.checkVisited(url)
            for i in range(mydb.getCount(title)):
                mainWord = myWords[i][1]
                textcolor = ";color:#FFFFFF'>"

                usedword = mainWord
                if visited:
                    # print("correct visited")
                    color = myWords[i][2]
                    if(color != 'NA'):
                        textcolor = ";color:#000000'>"
                    last = textcolor + mainWord + " </span>"
                    nextElement = "<span style='background-color: " + color + last
                    if(mainWord == 'NEWLINE'):
                        nextElement = '<br>'
                    elif(mainWord == 'BREAKBREAK'):
                        nextElement = '<br><br>'
                    finalAdd += nextElement
                else:
                    if not read_lyrics.knownWord(mainWord):
                        while (not read_lyrics.knownWord(usedword)) and len(usedword) > 1:
                            usedword = usedword[1:len(usedword)]

                    if read_lyrics.knownWord(usedword):
                        for j in range(1,15):
                            if i+j >= len(myWords):
                                break
                            newWord = myWords[i+j][1]
                            if(newWord == 'BREAKBREAK'):
                                break
                            if not read_lyrics.knownWord(newWord):
                                while (not read_lyrics.knownWord(newWord)) and len(newWord) > 1:
                                    newWord = newWord[1:len(newWord)]
                            if(read_lyrics.two_rhyme(usedword, newWord) >= 150):
                                # print(mydb.getColor(title, index))
                                if(myWords[i][2] == 'NA'):
                                    mydb.setColor(title, i,listColors[0])
                                    mydb.setColor(title, j+i,listColors[0])
                                    myWords[i][2] = listColors[0]
                                    myWords[i+j][2] = listColors[0]
                                    listColors.append(listColors.pop(0))
                                else:
                                    # mydb.setColor(title, index+i,mydb.getColor(title, index))
                                    mydb.setColor(title, j+i,myWords[i][2])
                                    myWords[i+j][2] = myWords[i][2]
                                # mydb.setColor(title,index-i, "#00FF00")

                        # myWord =  mydb.getWord(title, index);
                    color = myWords[i][2]
                    if(color != 'NA'):
                        textcolor = ";color:#000000'>"
                    last = textcolor + mainWord + " </span>"
                    nextElement = "<span style='background-color: " + color + last
                    if(mainWord == 'NEWLINE'):
                        nextElement = '<br>'
                    elif(mainWord == 'BREAKBREAK'):
                        nextElement = '<br><br>'
                    finalAdd += nextElement

        return finalAdd

if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host=HOST, port=PORT)
