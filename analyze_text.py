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
        text = text[2200:8100]
        #Because links are broken up into avalon base and the particular link must get in two parts
        links = re.findall(r'href="(.*?)asp',text)

        for link in links:
            rl = "http://avalon.law.yale.edu" + link[2:] + "asp"
            name = re.findall(r'century/(.*?).asp',url)
            speech = BeautifulSoup(requests.get(url).text, 'lxml')
            speech = str(speech.get_text())
            speech = speech[350:-470]
            f = open("Texts/" + name[0] + '.txt','w+')
            f.write(speech)
            f.close()

def analyze_text():
    """
    Analayze texts for sentiment
    """
    scores = []
    names = []
    poss =[]
    negs =[]
    for filename in os.listdir("/home/zneb/SoftDes/TextMining/Texts"):
            text = open("Texts/"+filename,'r')
            vs = analyzer.polarity_scores(text.read())
            name = filename.replace(".txt","")
            names.append(name)
            poss.append(vs['pos'])
            negs.append(vs['neg'])
    #         scores.append((name,"Positive: " + str(vs['pos']), "Negative: " + str(vs['neg'])))
    #         text.close()
    # scores.sort(key=lambda x: x[0])
    # for go in scores:
    #     print(go)
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
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='scores.png')


if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()
    #Base page
    url = "http://avalon.law.yale.edu/subject_menus/inaug.asp"
    #Collect texts
    collect_texts(url)
    scores = analyze_text()
    graph_scores(scores)
