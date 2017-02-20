"""
    Alex Chapman
    2/19/17

    Software Design Project 3

    Finding a list of U.S. Representatives and analyzing the sentiment of
    their respective wikipedia pages in corrolation with party affiliation.
"""

from lxml import html
import requests
import pickle
import wikipedia
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

sent = SentimentIntensityAnalyzer()


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_people(s):
    running = True
    senators = []
    num = 1
    while running:
        index_s = s.find(start_key)
        s = s[index_s:]
        index_e = s.find(end_key)
        chunk = s[:index_e]
        if index_s == -1 or index_e == -1:
            running = False
        if len(chunk) < 40:
            if ',' in chunk:
                senators.append(chunk[3:])
                num += 1
            s = s[index_e+3:]
        else:
            s = s[10:]
    return(senators[440:])


def eliminate_doubles(ls, result=[]):
    for name in ls:
        if name not in result:
            result.append(name)
    return result


def convert_accents(ls):
    blank = []
    for string in ls:
        if '&aacute;' in string:
            index = string.find('&aacute;')
            blank.append(string[:index] + 'a' + string[index+8:])
        elif '&eacute;' in string:
            index = string.find('&eacute;')
            blank.append(string[:index] + 'e' + string[index+8:])
        elif '&oacute;' in string:
            index = string.find('&oacute;')
            blank.append(string[:index] + 'o' + string[index+8:])
        else:
            blank.append(string)
    return blank


def remove_commas(ls):
    blank = []
    for string in ls:
        index = string.find(',')
        word = string[index+2:] + string[:index]
        blank.append(word)
    return blank


def look_up_people(ls):
    """
        Takes a list of politician's full names and finds them on wikipedia.
        Then goes through and analyzes this response, finding party
        affiliations and positivity / negaitivity of each article.

        Inputs: list of full names of senators
        Output: list of points containting sentiment scores
                list of values holding party affiliations

    """
    points = []
    # 1 for Dem, 0 for Rep, -1 for non-affiliated
    party_affiliation = []
    total = len(ls)
    for i, person in enumerate(ls):
        person = person + ' (U.S. politician)'
        print(str(int(i / total * 10000)/100) + '%')
        try:
            page_text = wikipedia.page(person).content
            to_test = wikipedia.summary(person)
            if'Democrat' in to_test:
                party_affiliation.append(1)
            elif 'Republican' in to_test:
                party_affiliation.append(0)
            else:
                party_affiliation.append(-1)
            hold = sentiment_analyze(page_text)
            points.append(hold)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e)
        except wikipedia.exceptions.PageError as e:
            pass
    pickle.dump(points, open("points.p", "wb"))
    pickle.dump(party_affiliation, open("party.p", "wb"))
    plot_values()


def plot_values():
    """
        Calculates and plots the average positivity / negativity values
        of each respective Congressmen's wikipedia page in terms of party
        affiliation.
        Inputs: None
        Prerequisites: Pickle variable containing the list of values,
                       Pickle variable containing list of party affiliations
        Output: Plot containing 435 red and blue points
    """
    points = pickle.load(open('points.p', 'rb'))
    party = pickle.load(open('party.p', 'rb'))
    dxvals = []
    dyvals = []
    rxvals = []
    ryvals = []
    uxvals = []
    uyvals = []
    for i, point in enumerate(points):
        pA = party[i]
        if pA == 1:
            dxvals.append(point.x)
            dyvals.append(point.y)
        elif pA == 0:
            rxvals.append(point.x)
            ryvals.append(point.y)
        else:
            uxvals.append(point.x)
            uyvals.append(point.y)
    plt.plot(dxvals, dyvals, 'bo')
    plt.plot(rxvals, ryvals, 'ro')
    plt.plot(uxvals, uyvals, 'co')
    plt.axis([0, .16, 0, .1])
    plt.show()


def sentiment_analyze(s):
    rating = sent.polarity_scores(s)
    a = Point(rating['pos'], rating['neg'])
    return a


def plot_average():
    """
        Calculates and plots the average positivity / negativity values
        of each respective Congressmen's wikipedia page in terms of party
        affiliation.
        Inputs: None
        Prerequisites: Pickle variable containing the list of values,
                       Pickle variable containing list of party affiliations
        Output: Plot containing a red and blue point

        As of 2/19/17 this showed blue slightly more positive than red, but
        just as negative
    """
    points = pickle.load(open('points.p', 'rb'))
    party = pickle.load(open('party.p', 'rb'))
    dc = 0
    rc = 0
    dx = 0
    dy = 0
    rx = 0
    ry = 0
    for i, point in enumerate(points):
        pA = party[i]
        if pA == 1:
            dx += point.x
            dy += point.y
            dc += 1
        elif pA == 0:
            rx += point.x
            ry += point.y
            rc += 1
    dx = dx / dc
    dy = dy / dc
    rx = rx / rc
    ry = ry / rc
    plt.plot(dx, dy, 'bo')
    plt.plot(rx, ry, 'ro')
    plt.axis([0, .16, 0, .1])
    plt.show()


"""test = pickle.load(open('senators.p', 'rb'))
for i in test:
    print(i + '/n')
look_up_people(test)"""


"""
d = {'&oacute;':'o','&aacute;':'a','&eacute;':'e'}
&oacute; -> o
&aacute; -> a
&eacute; -> e
"""
page = requests.get('http://www.house.gov/representatives/')
tree = html.fromstring(page.content)


start_key = '">'
end_key = '</a>'
to_process = page.content.decode("utf-8")
first_index = to_process.find(start_key)

"""print('Finding People')
sen = find_people(to_process)
print('Found People')
print('Processing Text')
sen = eliminate_doubles(sen)
sen = convert_accents(sen)
sen = remove_commas(sen)
print('Processed Text')
print('Saving List...')
pickle.dump(sen, open("senators.p", "wb"))"""

# look_up_people(sen)
plot_values()
plot_average()
