import pronouncing

def analyze_text(myString):
    myString = myString.replace(",", "")
    myString = myString.replace(".", "")
    myString = myString.replace("?", "")
    myList = myString.split(" ")
    running = []
    running.append(myList[0])

    idk = 0
    same = 0
    usedRhymes = []
    for i in range(1, len(myList)):
        for j in running:
            if not usedRhymes.__contains__(j + myList[i]):
                usedRhymes.append(j + myList[i])
                rating = two_rhyme(j, myList[i])
                if rating == -1:
                    while two_rhyme(j, myList[i]) == -1 and len(myList[i]) > 1:
                        myList[i] = myList[i][1:len(myList[i])]
                    if two_rhyme(j, myList[i]) == -1:
                        idk += 1
                        break
                if rating >= 100:
                    same += 1
                    print(j + ' ' + myList[i])

        running.append(myList[i])
        if len(running) > 15:
            running.pop(0)

    print(idk)
    rate = same / len(myList)
    return same, len(myList)


def two_rhyme(Sinit, Sinit2):
    St1 = Sinit.lower()
    St2 = Sinit2.lower()
    if St1 == St2:
        return 0
    St1 = St1.replace("in'", "ing")
    St2 = St2.replace("in'", "ing")
    St1 = pronouncing.phones_for_word(St1)
    St2 = pronouncing.phones_for_word(St2)

    if len(St1) == 0:
        #print(Sinit)
        return 0
    elif len(St2) == 0:
        #print(Sinit2)
        return -1
    else:
        s1 = convert_phon(St1[0])
        s2 = convert_phon(St2[0])
        return find_sim(s1, s2)


def find_sim(s1, s2):
    score = 0
    for i in range(1, 4):
        if(len(s1) < i or len(s2) < i):
            break
        if(s1[len(s1) - i] == s2[len(s2) - i]):
            score += 100
        if(i > 1):
            if(s1[len(s1) - i] == s2[len(s2) - i + 1]):
                score += 50
        if(not len(s2) < i + 1):
            if(s1[len(s1) - i] == s2[len(s2) - i - 1]):
                score += 50
    return score


def convert_phon(myString):
    myString = myString.replace("0", "")
    myString = myString.replace("1", "")
    myString = myString.replace("2", "")
    return myString.split(" ")


def rhyme_finder(url):
    html = BeautifulSoup(requests.get(url).text, 'lxml')
    totR = 0
    totW = 0
    for par in html.find_all('p', 'verse'):  # find the first paragraph
        print(par.get_text())
        r, w = analyze_text(par.get_text())
        print(100 * r/w)
        totR += r
        totW += w
    print("Total Rhyme Rate")
    print(100 * totR/totW)
    #str(html.find('p'))  # the first paragraph, as a string. Includes embedded <b> etc.


if __name__ == '__main__':
    import pronouncing
    # print(pronouncing.phones_for_word("permit"))
    # print(analyze_text("His palms are sweaty, knees weak, arms are heavy. There's vomit on his sweater already, mom's spaghetti"))
    # print(analyze_text("Sometimes I like to walk in the park especially enjoy the fresh air and birds signing. After I go, I feel good"))
    from bs4 import BeautifulSoup
    import requests
    rhyme_finder('http://www.metrolyrics.com/ive-got-you-under-my-skin-lyrics-frank-sinatra.html')
