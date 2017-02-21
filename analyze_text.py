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
    for filename in os.listdir("/home/zneb/SoftDes/TextMining/Texts"):
            text = open("Texts/"+filename,'r')
            speech = text.read()
            text.close()


if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()
    #Base page
    url = "http://avalon.law.yale.edu/subject_menus/inaug.asp"
    #Collect texts
    collect_texts(url)
    analyze_text()
