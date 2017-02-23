import wikipedia
import nltk
import string
page1=wikipedia.page('Olin College')
list1=nltk.word_tokenize(page1.content)
page2=wikipedia.page('Stanford University')
list2=nltk.word_tokenize(page2.content)
concatlist1=[]
concatlist2[]

def no_repeat(list1, list2):
    for i in list1:
        if i not in concatlist1:
            concatlist1.append(i)
    for i in list2:
        if i not in concatlist2:
            concatlist2.append(i)
    return concatlist1, concatlist2

compiled=[]
def similarity(concatlist1, concatlist2):
    i=0
    for i in list1[i]:
        if list1[i] in list2:
            compiled.append[list1]
        else:
            i+=1
    return compiled
