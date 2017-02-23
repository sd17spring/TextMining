"""
Software Desgin 2017
Text Mining Project

Takes each president's inaugural addresses and compares their sentiments.
The data is then plotted. Can be used to gauge the previous president's term.

@author: Benjamin Ziemann, github: zneb97
"""
import requests
import os
import sys
import pickle
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import plotly

#Get plotly api key
keyFile = open('plotlyAPIKey.txt','r')
plotlyAPIKey = keyFile.read().strip()
keyFile.close()
plotly.tools.set_credentials_file(username='zneb97', api_key=plotlyAPIKey)

import plotly.plotly as py
import plotly.graph_objs as go

def collect_texts(page):
    """
    Collect the texts of all presidental inaugural adresses and save
    them if they do not already exist
    """
    #Check to see if the files already exist
    if not os.path.exists("Texts/wash1.txt"):
        #Texts are all linked from a central page
        html = BeautifulSoup(requests.get(page).text, 'lxml')
        text = str(html)
        text = text[2200:8150]
        #Because links are broken up into avalon base and the particular link must get in two parts
        links = re.findall(r'href="(.*?)asp',text)
        #Get dates for later sorting use
        dates = re.findall(r'">(.*?)</a>',text)
        for i in range(len(links)):
            url = "http://avalon.law.yale.edu" + links[i][2:] + "asp"
            name = re.findall(r'century/(.*?).asp',url)
            speech = BeautifulSoup(requests.get(url).text, 'lxml')
            speech = str(speech.get_text())
            speech = speech[360:-470]
            f = open("Texts/" + name[0] + '.txt','w+')
            f.write(dates[i] + " " + speech)
            f.close()

def analyze_text():
    """
    Analayze texts for sentiment
    """
    data = []
    scores = []
    names = []
    dates = []
    poss =[]
    negs =[]
    for filename in os.listdir("/home/zneb/SoftDes/TextMining/Texts"):
            text = open("Texts/"+filename,'r')
            date = text.read()[0:4]
            text.seek(0) #Resets the reading
            vs = analyzer.polarity_scores(text.read())
            if not vs['pos'] == 0:
                name = filename.replace(".txt","")
                data.append((name,date,vs['pos'],vs['neg']))
    #Various data sorts. Uncomment as needed
    #data.sort(key=lambda x: x[0])  #Sort alphabetically by name
    data.sort(key=lambda x: x[1])  #Sort date
    #data.sort(key=lambda x: x[2])  #Sort by positivity
    #data.sort(key=lambda x: x[3])  #Sort by negativity

    #Break into seperate arrays to be used in graph
    for tup in data:
        names.append(tup[0])
        dates.append(tup[1])
        poss.append(tup[2])
        negs.append(tup[3])
    scores = [names,poss,negs]
    return scores

def graph_scores(scores):
    trace1 = go.Bar(
        x=scores[0],
        y=scores[1],
        name='Positive Score'
    )
    trace2 = go.Bar(
        x=scores[0],
        y=scores[2],
        name='Negative Score'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group',
        width = 1000,
        title='Sentiment of Inaugural Speeches',
        xaxis=dict(
        nticks = 60,
        title='President',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#000000'
        )
    ),
    yaxis=dict(
        title='Value',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#000000'
        )
    )
    )

    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='scores.png')


if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()
    #Base page
    url = "http://avalon.law.yale.edu/subject_menus/inaug.asp"
    collect_texts(url)
    scores = analyze_text()
    graph_scores(scores)
