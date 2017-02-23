import pickle
from bs4 import BeautifulSoup


input_file = open('cnn.pickle', 'rb')
cnnwebsite = pickle.load(input_file)

soup = BeautifulSoup(cnnwebsite, "html.parser")

text = soup.get_text()
count = 0
text = text.split()
for i in text:
    if(i == "trump" or i == "Trump" or i == ""):
        count += 1
print(count)
