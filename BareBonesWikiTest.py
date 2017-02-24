import pickle as pk
#import lxml.etree
import re
import urllib.parse as ulps
import urllib.request as ulrq
import bs4
from random import choice
from collections import Counter
import operator
import nltk
from string import punctuation

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def savetxt(filename, data, lks=[], ls_lks=[]):
    f = open('pickles//' + filename.replace(" ","").replace("/","") + '.pickle','wb')
    links_txt = "\n".join(lks)
    ls_links_txt = "\n".join(ls_lks)
    datadump = "\n".join(["==Title==", filename, "", "==Content==", data, "", "==Links==", links_txt, "", "==List Links==", ls_links_txt])
    pk.dump(datadump, f)
    f.close()

def savehtml(filename, data, lks=[], ls_lks=[]):
    f = open('htmls//' + filename.replace(" ","").replace("/","") + '.html','wb')
    pk.dump(data, f)
    f.close()

def loadhtml(filename):
    try:
        input_file = open('htmls//' + filename.replace(" ","").replace("/","//") + '.html','rb')
        loaded = pk.load(input_file)
        return loaded
    except:
        return None

def loadtxt(filename):
    # Load data from a file (will be part of your data processing script)
    input_file = open('pickles//' + filename.replace("/","") + '.pickle','rb')
    loaded = pk.load(input_file)
    return loaded

def cleanHtml(pat, rd):
    rdlis= re.findall(pat, rd)
    inter_rd = b'\n'.join(rdlis)
    rm_attribs = [b'<i>', b'</i>', b'<b>', b'</b>']
    pat_rd = re.compile(b'|'.join(rm_attribs))
    newrd = re.sub(pat_rd, b'', inter_rd)
    return newrd

def cleanHtmlExtra(pat, rd):
    rdlis= re.findall(pat, rd)
    #print(rdlis[0])
    inter1_rd = b'\n'.join(rdlis)
    end_sep = b'<h2><span class="mw-headline" id="References">References'
    inter_rd= inter1_rd.split(end_sep, 1)[0]
    rm_attribs = [b'<i>', b'</i>', b'<b>', b'</b>']#, b'<p>', b'</p>', b'<a>', b'</a>', b'<li>', b'</li>']
    pat_rd = re.compile(b'|'.join(rm_attribs))
    new_rd = re.sub(pat_rd, b'', inter_rd)
    #print(new_rd_pre)
    print('len: ' + str(len(inter_rd)) + '  /  ' + str(len(inter1_rd)))
    return new_rd

def txtlist(target_link):
    webpage = ulrq.urlopen(target_link)

    rd_target = webpage.read()

    pat_target = re.compile(b'(<p>.*|<li>.*|<h1>.*|<h2>.*)')
    newrd = cleanHtmlExtra(pat_target, rd_target)
    soup_target = bs4.BeautifulSoup(newrd, 'html.parser')
    return soup_target.get_text()

def nxtlink(startLink, numLinks, langs, target):
    i = 0
    nextlink = startLink
    firstLinkList = []
    Titles = []
    linkprefix = "https://en.wikipedia.org"
    target_link = linkprefix+"/wiki/"+"_".join(target.split())

    while i < numLinks:

        #Parse
        webpage = ulrq.urlopen(nextlink)

        rd = webpage.read()

        pat = re.compile(b'<p>.*')
        pat_ls = re.compile(b'<li>.*')
        newrd = cleanHtml(pat, rd)
        #print(newrd)

        souporig = bs4.BeautifulSoup(rd, "html.parser")
        soup = bs4.BeautifulSoup(newrd, "html.parser")


        titlefind = souporig.findAll('h1', attrs={'class': re.compile("firstHeading")})
        title = (titlefind[0].get_text())

        print(str(i) + '\t' + title)
        links = []
        Non_links = ["File:", "Help:","Category:","Wikipedia:"]
        #negate_links = langs + Non_links
        href_regex_str = "^/wiki/(?!"+"|".join(Non_links)+").*"
        #text_regex_str = "^(?!"+"|.*".join(langs)+".*"+")"
        text_regex_str = "^(?!(.*\s)?"+"((\s.*)|$)|(.*\s)?".join(langs)+"((\s.*)|$)"+").*"
        for link in soup.findAll('a', attrs={'href': re.compile(href_regex_str)}, text=re.compile(text_regex_str)):
            links.append(link.get('href'))
            #print(link.get('href'))

        ls_links = []
        retry_rd = cleanHtml(pat_ls, rd)
        soup_ls = bs4.BeautifulSoup(retry_rd, "html.parser")
        for link in soup_ls.findAll('a', attrs={'href': re.compile(href_regex_str)}, text=re.compile(text_regex_str)):
            ls_links.append(link.get('href'))

        print(souporig.get_text())

        Titles.append(title)
        savetxt(title, soup.get_text(), lks = links, ls_lks = ls_links)
        savehtml(title, rd)
        if title == target:
            print('Finished!')
            print('Found ' + target + '!!')
            return Titles
        if i > 0 and title in Titles[:i]:
            tIndex = Titles.index(title)
            print('Finished!')
            print('Found Circular Dependency with following articles:')
            print(' --> '.join(Titles[tIndex:]))
            return Titles
        ##get first link excluding languages
        #print(newlink)
        if len(links) > 0:
            newlink = links[0]
        elif len(ls_links)>0:
            newlink = ls_links[0]
        else:
            print("Finished!")
            print("Couldn't find anymore links in " + title)
            return Titles
        firstLinkList.append(newlink)
        nextlink = linkprefix+newlink
        i += 1
    print('Finished!')
    print("Didn't find your article")
    return Titles


def randlink(startLink, numLinks, paragraph_link_prefer = False):
    i = 0
    nextlink = startLink
    takenLinkList = []
    Titles = []
    linkprefix = "https://en.wikipedia.org"
    while i < numLinks:
        webpage = ulrq.urlopen(nextlink)

        rd = webpage.read()

        pat = re.compile(b'<p>.*')
        pat_ls = re.compile(b'<li>.*')
        newrd = cleanHtml(pat, rd)
        #print(newrd)

        souporig = bs4.BeautifulSoup(rd, "html.parser")
        soup = bs4.BeautifulSoup(newrd, "html.parser")


        titlefind = souporig.findAll('h1', attrs={'class': re.compile("firstHeading")})
        title = (titlefind[0].get_text())

        print(str(i) + '\t' + title)
        links = []
        Non_links = ["File:", "Help:","Category:","Wikipedia:"]
        #negate_links = langs + Non_links
        href_regex_str = "^/wiki/(?!"+"|".join(Non_links)+").*"
        #text_regex_str = "^(?!"+"|.*".join(langs)+".*"+")"
        #text_regex_str = "^(?!(.*\s)?"+"((\s.*)|$)|(.*\s)?".join(langs)+"((\s.*)|$)"+").*"
        for link in soup.findAll('a', attrs={'href': re.compile(href_regex_str)}):#, text=re.compile(text_regex_str)):
            links.append(link.get('href'))
            #print(link.get('href'))

        ls_links = []
        retry_rd = cleanHtml(pat_ls, rd)
        soup_ls = bs4.BeautifulSoup(retry_rd, "html.parser")
        for link in soup_ls.findAll('a', attrs={'href': re.compile(href_regex_str)}):#, text=re.compile(text_regex_str)):
            ls_links.append(link.get('href'))

        #print(souporig.get_text())

        Titles.append(title)
        savetxt(title, soup.get_text(), lks = links, ls_lks = ls_links)
        savehtml(title, rd)
        #if title == target:
        #    print('Finished!')
        #    print('Found ' + target + '!!')
        #    return Titles
        #if i > 0 and title in Titles[:i]:
        #    tIndex = Titles.index(title)
        #    print('Finished!')
        #    print('Found Circular Dependency with following articles:')
        #    print(' --> '.join(Titles[tIndex:]))
        #    return Titles
        ##get first link excluding languages
        #print(newlink)links_all = links + ls_links
        if paragraph_link_prefer:
            if len(links) > 0:
                newlink = choice(links)
            elif len(ls_links) > 0:
                newlink = choice(ls_links)
            else:
                print("Finished!")
                print("Couldn't find anymore links in " + title)
                return Titles
        else:
            links_all = links + ls_links
            if len(links_all) > 0:
                newlink = choice(links_all)
            else:
                print("Finished!")
                print("Couldn't find anymore links in " + title)
                return Titles
        takenLinkList.append(newlink)
        nextlink = linkprefix+newlink
        i += 1
    print('Finished!')
    #print("Didn't find your article")
    return Titles


def wikiFind(start, numLinks, langs, target, disallowedkeys):
    i = 0
    linkprefix = "https://en.wikipedia.org" # Link prefix for every link to be added to
    target_link_suffix = "/wiki/"+"_".join(target.split())
    target_link = linkprefix+target_link_suffix #Target links
    start_link_suffix = "/wiki/"+"_".join(start.split())
    start_link = linkprefix+start_link_suffix
    nextlink = start_link #Make Start Link Next Links
    LinkList = [] #Instantiate list of links clicked
    #lnk_names = [] #Text names of links
    checkList = []
    Titles = [] # Instantiate list of titles

    #Parse Target Link

    target_txt = txtlist(target_link).lower() #list of text in target html
    #print(target_txt)
    word_ls = [x for x in strip_punctuation(target_txt).split() if len(x) > 2] # list of words in target html
    freq_target = Counter(word_ls) #Frequency of words in target html
    #print(freq_target)
    targetwordsnorm = [x for x in strip_punctuation(target).split()]
    targetwords = [x.lower() for x in targetwordsnorm]
    #target_title_length = len(targetwords)
    for s in targetwords:
        if len(s) > 2: freq_target[s.lower()] = freq_target.get(s.lower(), 0) + 30
    #req_target_keys = freq_target.keys()
    #print(type(freq_sort_dict))
    #print(type(freq_sort_dict[0::2]))
    tagged_keys = nltk.pos_tag(freq_target.keys())

    approved_word_types = ["NN","NNP","NP","NNS","JJ"]
    for tup in tagged_keys:
        if tup[0] in targetwords:
            ind=targetwords.index(tup[0])
            if not targetwordsnorm[ind].islower():
                continue
        if not tup[1] in approved_word_types or tup[0] in disallowedkeys:
            del freq_target[tup[0]]

    freq_sort_dict=sorted(freq_target.items(), key=operator.itemgetter(1), reverse=True)
    for item in freq_sort_dict:
        for item2 in freq_sort_dict:
            if item[0] == item2[0]+'s'or item[0] == item2[0][:-1]+'ies':
                if item[1] > item2[1]:
                    try:
                        freq_sort_dict.remove(item2)
                        #print(item2[0] + " was deleted")
                    except:
                        print(item2[0] + " was already deleted")
                else:
                    try:
                        freq_sort_dict.remove(item)
                        #print(item[0] + " was deleted")
                    except:
                        print(item[0] + " was already deleted")
    #print(freq_sort_dict)

    ignore_txt = ''
    while i < numLinks:

        #Parse
        #Prefer using already saved html
        nxlnkprefix = linkprefix+"/wiki/"
        search_title = nextlink[len(nxlnkprefix):].replace("_", "")#.replace(":","%3") #Do need second one?
        #print("THIS IS SEARCH TITLE: "+ search_title)
        curhtml = loadhtml(search_title)
        if curhtml != None:
            print("Retrieving from Files")
            rd = curhtml
        else:
            webpage = ulrq.urlopen(nextlink)

            rd = webpage.read()

        pat = re.compile(b'(<p>.*|<li>.*)')
        newrd = cleanHtml(pat, rd)
        #print(newrd)

        souporig = bs4.BeautifulSoup(rd, "html.parser")
        soup = bs4.BeautifulSoup(newrd, "html.parser")


        titlefind = souporig.findAll('h1', attrs={'class': re.compile("firstHeading")})
        title = strip_punctuation(titlefind[0].get_text()) #should strip punctuation or no????!!!?!?!?

        print(str(i) + '\t' + title + "\n")
        links = {}
        Non_links = ["File:", "Help:","Category:","Wikipedia:"]
        #negate_links = langs + Non_links
        href_regex_str = "^/wiki/(?!"+"|".join(Non_links)+").*"
        #text_regex_str = "^(?!"+"|.*".join(langs)+".*"+")"
        #text_regex_str = "^(?!(.*\s)?"+"((\s.*)|$)|(.*\s)?".join(langs)+"((\s.*)|$)"+").*"
        for link in soup.findAll('a', attrs={'href': re.compile(href_regex_str)}): #text=re.compile(text_regex_str)):
            links[link.get_text()]=(link.get('href'))
            #print(link.get('href'))

        #ls_links = {}
        #retry_rd = cleanHtml(pat_ls, rd)
        #soup_ls = bs4.BeautifulSoup(retry_rd, "html.parser")
        #for link in soup_ls.findAll('a', attrs={'href': re.compile(href_regex_str)}, text=re.compile(text_regex_str)):
        #    ls_links.append(link.get('href'))

        #print(souporig.get_text())

        Titles.append(title)
        savetxt(title, soup.get_text())
        savehtml(title, rd)
        if title.lower() == strip_punctuation(target).lower():
            print('Finished!')
            print('Found ' + target + '!!')
            return Titles
        #if i > 0 and title in Titles[:i]:
        #    tIndex = Titles.index(title)
        #    print('Finished!')
        #    print('Found Circular Dependency with following articles:')
        #    print(' --> '.join(Titles[tIndex:]))
        #    return Titles
        ##get first link excluding languages
        #print(newlink)
        found = False
        for lnk_comp, lnk, in links.items():
            if lnk.lower() == target_link_suffix.lower():
                newlink = lnk
                found = True
                break

        if not found and len(checkList) > 1 and checkList[-1] == checkList[-2]:
            ignore_txt = checkList[-1]
        else:
            ignore_txt = ''

        lnks = []
        if not found:
            if len(links) > 0:
                #Algorithm for deciding next link
                for txt, freq in freq_sort_dict: #Iterate through freq_target by word frequency
                    if txt == ignore_txt or freq < 2:
                        continue
                    for lnk_comp, lnk in links.items(): #Iterate randomly through list of links
                        for lnk_txt in lnk_comp.split(): # Split links into singular words and iterate through those
                            if txt == strip_punctuation(lnk_txt).lower() and not lnk in LinkList: # SHOULD I STRIP PUCTUATION??#If txt and linktxt are the same and the link isn't the same
                                lnks.append(lnk)
                                checkList.append(txt)
                                found = True
                                #print("found optimal link")
                    if found:
                        lnks.sort(key = len)
                        print("Searched Word: " + checkList[-1] + "\t" + str(freq))
                        newlink = lnks[0]
                        break
                if not found:
                    print("randomly chose link")
                    newlink_txt,newlink = choice(list(links.items()))
            else:
                print("Finished!")
                print("Couldn't find anymore links in " + title)
                return Titles
        LinkList.append(newlink)
        nextlink = linkprefix+newlink
        i += 1
    print('Finished!')
    print("Didn't find your article")
    return Titles
#prop=links%7Crevisions&titles=Mass+production&redirects=1&pllimit=500&rvprop=content



#params = { "format":"xml", "action":"query", "prop":"links%7Crevisions","pllimit":"500", "rvprop":"content" } #Sets up list of items
#params["titles"] = "API|%s" % ulps.quote(title.encode("utf8"))
#qs = "&".join("%s=%s" % (k, v)  for k, v in params.items())
#url = "http://en.wikipedia.org/w/api.php?%s" % qs
#params = { "format":"xml", "action":"query", "prop":"revisions","rvprop":"content" } #Sets up list of items
#params["titles"] = "API|%s" % ulps.quote(title.encode("utf8"))
#qs = "&".join("%s=%s" % (k, v)  for k, v in params.items())
#url = "http://en.wikipedia.org/w/api.php?%s" % qs
#params1 = { "format":"json", "action":"query", "prop":"links","pllimit":"500" } #Sets up list of items
#params1["titles"] = "API|%s" % ulps.quote(title.encode("utf8"))
#qs1 = "&".join("%s=%s" % (k, v)  for k, v in params1.items())
#url1 = "http://en.wikipedia.org/w/api.php?%s" % qs1
#print(url)
#webpage = ulrq.urlopen(url)
#webpage1 = ulrq.urlopen(url1)
langlist ="""Afrikaans 	AF
Albanian 	SQ
Arabic 	AR
Armenian 	HY
Basque 	EU
Bengali 	BN
Bulgarian 	BG
Catalan 	CA
Cambodian 	KM
Chinese 	ZH
Croatian 	HR
Czech 	CS
Danish 	DA
Dutch 	NL
English 	EN
Estonian 	ET
Fiji 	FJ
Finnish 	FI
French 	FR
Georgian 	KA
German 	DE
Greek 	EL
Gujarati 	GU
Hebrew 	HE
Hindi 	HI
Hungarian 	HU
Icelandic 	IS
Indonesian 	ID
Irish 	GA
Italian 	IT
Japanese 	JA
Javanese 	JW
Korean 	KO
Latin 	LA
Latvian 	LV
Lithuanian 	LT
Macedonian 	MK
Malay 	MS
Malayalam 	ML
Maltese 	MT
Maori 	MI
Marathi 	MR
Mongolian 	MN
Nepali 	NE
Norwegian 	NO
Persian 	FA
Polish 	PL
Portuguese 	PT
Punjabi 	PA
Quechua 	QU
Romanian 	RO
Russian 	RU
Samoan 	SM
Serbian 	SR
Slovak 	SK
Slovenian 	SL
Spanish 	ES
Swahili 	SW
Swedish  	SV
Tamil 	TA
Tatar 	TT
Telugu 	TE
Thai 	TH
Tibetan 	BO
Tonga 	TO
Turkish 	TR
Ukrainian 	UK
Urdu 	UR
Uzbek 	UZ
Vietnamese 	VI
Welsh 	CY
Xhosa 	XH   US  or  and"""

langs = langlist.split()
disallowedkeys = ["many","use", "such", "other", "first"]
while True:
    start = input("Enter Start Title (Capitolize): ")
    end = input("Enter End Title (Capitolize): ")
    wikiFind(start, 45, langs, end, disallowedkeys)#, disallowedkeys)

#randlink(start, 10, paragraph_link_prefer = True)
