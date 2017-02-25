# Load data from a file (will be part of your data processing script)
import pickle
import math
import io
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#tested setup by printing requests
def setup():
    import requests
    shaw_full_text = requests.get('http://www.gutenberg.org/cache/epub/3825/pg3825.txt').text
    import pickle
    # Save data to a file (will be part of your data fetching script)
    f = open('shaw_texts.pickle', 'wb')
    pickle.dump(shaw_full_text, f)
    f.close()

#tested this by printing copy of texts
def setup_functionality():

    import pickle
    input_file = open('shaw_texts.pickle', 'rb')
    copy_of_texts_from_pickel = pickle.load(input_file)
    Higgins_lines = []
    Liza_lines = []
    Freddy_lines = []
    play_lines = copy_of_texts_from_pickel.split('\r\n\r\n')
    #used a print of play_lines to check if this was mostly working. It was but there are some errors that are minor.
    #if I had more time I would fix those.
    for line in play_lines:
        if line[0:7] == "HIGGINS":
            Higgins_lines.append(line)
        elif line[0:15] == "THE FLOWER GIRL" or line[0:4] == "LIZA":
            Liza_lines.append(line)
        elif line[0:6] == "FREDDY":
            Freddy_lines.append(line)
    a = [Higgins_lines, Liza_lines, Freddy_lines]
    return a
#returned lines ot make sure they individually worked.

def Sentinment_Anlyis(someone_lines):
    #had to test if array was working.
    analyzer = SentimentIntensityAnalyzer()
    someone_neu=[]
    someone_pos=[]
    someone_neg=[]
    someone_cmpd=[]
    for sentence in someone_lines:
        scores = analyzer.polarity_scores(sentence)
        someone_neu.append(scores['neu'])
        someone_pos.append(scores['pos'])
        someone_neg.append(scores['neg'])
        someone_cmpd.append(scores['compound'])
        #made sure this was working by printing these
    someone_neu_avg = sum(someone_neu)/len(someone_neu)
    someone_pos_avg = sum(someone_pos)/len(someone_pos)
    someone_neg_avg = sum(someone_neg)/len(someone_neg)
    someone_cmpd_avg = sum(someone_cmpd)/len(someone_cmpd)
    someone_avg_all = [someone_neu_avg, someone_pos_avg, someone_neg_avg, someone_cmpd_avg]
    print(someone_avg_all)

def analyze_all_lines():
    #Line below can be commented/uncommented based on if you have the text alread.
    #This is is to limit the number of requests.
    #originally I had but this in another file
    #setup()
    #a is the array output of higgins, liza, Freddy in that order
    #also I'm kind of unsur eabout how/where to use docstrings so I checked via printing? Esp since the text was so long.
    a = setup_functionality()
    Sentinment_Anlyis(a[0])
    Sentinment_Anlyis(a[1])
    Sentinment_Anlyis(a[2])
    # Sentinment_Anlyis(Liza_lines)
    # Sentinment_Anlyis(Freddy_lines)


analyze_all_lines()
