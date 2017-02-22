"""
    Alex Chapman
    2/19/17

    Software Design Project 3

    Finding a list of U.S. Representatives and analyzing the sentiment of
    their respective wikipedia pages in corrolation with party affiliation.
"""

import requests
import pickle
import wikipedia
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

sent = SentimentIntensityAnalyzer()
rep_normalized = 0
dem_normalized = 0


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_people(s):
    """
        Parses through the html of the US Government page looking for specific
        tags that reference names of politicians. Then calls slave functions
        eliminate_doubles, conver_accents, and remove_commas to properly
        format the resulting list of names.

        Input: raw html in string form
        Output: Clean list of names
    """
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
    sen = senators[440:]
    return remove_commas(convert_accents(eliminate_doubles(sen)))


def eliminate_doubles(ls, result=[]):
    """
        Web Page is formatted such that the index of all names is mixed
        with the actual text, thus in order to strip the correct number of
        politicians you must eliminate the doubles. This goes through the
        primary list and returns a version of it with all doubles eliminated
    """
    for name in ls:
        if name not in result:
            result.append(name)
    return result


def convert_accents(ls):
    """
        Finds and replaces all accented characters within the names of
        the US politicians represented in the input list

        Input: Full list of Politicians
        Output: Full list of correctly formatted politicians
    """
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
    """
        Takes a list of names in format Last, First and converts to
        First Last format

        Input: Full list of Politicians
        Output: Full list of correctly formatted politicians
    """
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
        affiliations and positivity / negativity of each article.

        Inputs: list of full names of senators
        Output: list of points containting sentiment scores
                list of values holding party affiliations

    """
    dem_totals = 0
    dem_num = 0
    rep_totals = 0
    rep_num = 0

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
                dem_num += 1
                dem_totals += sentiment_analyze_overall(page_text)
            elif 'Republican' in to_test:
                party_affiliation.append(0)
                rep_num += 1
                rep_totals += sentiment_analyze_overall(page_text)
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
    rep_normalized = rep_totals / rep_num
    dem_normalized = dem_totals / dem_num
    print('Republican Net Score: ', rep_normalized)
    print('Democrat Net Score: ', dem_normalized)
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
    plt.axis([0, .16, 0, .1])
    plt.ylabel('Negativity')
    plt.xlabel('Positivity')
    plt.title('Sentiment Values for Republicans and Democrats')
    plt.show()


def sentiment_analyze(s):
    rating = sent.polarity_scores(s)
    a = Point(rating['pos'], rating['neg'])
    return a


def sentiment_analyze_overall(s):
    rating = sent.polarity_scores(s)
    a = rating['compound']
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
    plt.ylabel('Negativity')
    plt.xlabel('Positivity')
    plt.title('Average Sentiment Values for Republicans and Democrats')

    plt.show()


if __name__ == '__main__':
    """
        Main section. This .py file contains all code necessary to run the
        project. Necessary pickle files are included so as to make run time
        shorter (does not actually call wikipedia in current form). In order
        to get the full functionality uncomment the line "look_up_poeple()"

        Republican and Democrat net score represent their respective cumulative
        scores.
    """
    print("This only executes when %s is executed rather than imported")
    """
        d = {'&oacute;':'o','&aacute;':'a','&eacute;':'e'}
        &oacute; -> o
        &aacute; -> a
        &eacute; -> e

        Republican Net Score:  0.7759978835978834
        Democrat Net Score:    0.8074467980295562

    """
    page = requests.get('http://www.house.gov/representatives/')

    start_key = '">'
    end_key = '</a>'
    to_process = page.content.decode("utf-8")
    """
        print('Finding People')
        sen = find_people(to_process)
        print('Republican Net Score: ', rep_normalized)
        print('Democrat Net Score: ', dem_normalized)
        pickle.dump(sen, open("senators.p", "wb"))
    """

    # look_up_people(sen)
    plot_values()
    plot_average()
