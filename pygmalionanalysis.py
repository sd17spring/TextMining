# Load data from a file (will be part of your data processing script)
import pickle
import math
import io
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def setup():
    import requests
    shaw_full_text = requests.get('http://www.gutenberg.org/cache/epub/3825/pg3825.txt').text
    print(shaw_full_text)
    import pickle
    # Save data to a file (will be part of your data fetching script)
    f = open('shaw_texts.pickle', 'wb')
    pickle.dump(shaw_full_text, f)
    f.close()


def setup_functionality():
    import pickle
    input_file = open('shaw_texts.pickle', 'rb')
    copy_of_texts_from_pickel = pickle.load(input_file)
    # print(copy_of_texts_from_pickel)
    # blob= open('copy_of_texts').readline()
    Higgins_lines = []
    Liza_lines = []
    Freddy_lines = []
    play_lines = copy_of_texts_from_pickel.split('\r\n\r\n')
    #print(play_lines)
    for line in play_lines:
        if line[0:7] == "HIGGINS":
            Higgins_lines.append(line)
        elif line[0:15] == "THE FLOWER GIRL" or line[0:4] == "LIZA":
            Liza_lines.append(line)
        elif line[0:6] == "FREDDY":
            Freddy_lines.append(line)
    a = [Higgins_lines, Liza_lines, Freddy_lines]
    return a
    # return Higgins_lines
    # return Liza_lines
    # return Freddy_lines
    # print(Liza_lines)
    # print(Freddy_lines)
    # print(Higgins_lines)

def Sentinment_Anlyis(someone_lines):
    analyzer = SentimentIntensityAnalyzer(someone_lines)
    #total_score = []
    someone_neu=[]
    someone_pos=[]
    someone_neg=[]
    someone_cmpd=[]
    for sentence in someone_lines:
        scores = analyzer.polarity_scores(sentence)
        someone_neu.append(scores['neu'])
        someone_pos.append(score['pos'])
        someone_neg.append(score['neg'])
        someone_cmpd.append(score['compound'])


        #print(Freddy_neu)
        #scores['pos']
        #scores['neg']
        #scores['compound']
        #total_score.append(scores)
    #print(total_score)
    someone_neu_avg = sum(someone_neu)/len(someone_neu)
    someone_pos_avg = sum(someone_pos)/len(someone_pos)
    someone_neg_avg = sum(someone_neg)/len(someone_neg)
    someone_cmpd_avg = sum(someone_cmpd)/len(someone_cmpd)
    someone_avg_all = [someone_neu_avg, someone_pos_avg, someone_neg_avg, someone_cmpd_avg]
    print(someone_avg_all)
#print(Freddy_neu_avg)
#     b = Higginsscrip\
# lines=[]
# for line in blob:
#     lines.append(line)
# print(lines)

# buf = io.StringIO(copy_of_texts_from_pickel)

def analyze_all_lines():
#if __name__ == '__main__':
    #setup()
    a = setup_functionality()
    b=a[1]
    print(b)
    Sentinment_Anlyis(b)
    # Sentinment_Anlyis(Liza_lines)
    # Sentinment_Anlyis(Freddy_lines)


analyze_all_lines()
