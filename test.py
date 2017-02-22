import requests
import pickle
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import os


# html = BeautifulSoup(requests.get("http://avalon.law.yale.edu/subject_menus/inaug.asp").text, 'lxml')
# text = str(html)
# text = text[2200:8100]
# x = re.findall(r'href="(.*?)asp',text)
# print(x)
# for link in x:
#     url = "http://avalon.law.yale.edu" + link[2:] + "asp"
#     name = re.findall(r'century/(.*?).asp',url)
#     speech = BeautifulSoup(requests.get(url).text, 'lxml')
#     speech = str(speech.get_text())
#     speech = speech[350:-470]
#     f = open("Texts/" + name[0] + '.txt','w+')
#     f.write(speech)
#     f.close
print("testing git ignroe")
names = []
for filename in os.listdir("/home/zneb/SoftDes/TextMining/Texts"):
    speech = open("Texts/"+filename,'r')
    print(speech.read())
    speech.close()
    names.append(filename)
print(names)
