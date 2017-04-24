from classText import Text

"""
Finding  the longest word
"""

geschwister = Text('Die Geschwister', 'Johann Wolfgang von Goethe', 'geschwister.txt')
berlichingen = Text('Götz von Berlichingen', 'Johann Wolfgang von Goethe', 'berlichingen.txt')
iphigenie = Text('Iphigenie auf Tauris', 'Johann Wolfgang von Goethe', 'iphigenie.txt')
reinekefuchs = Text('Reineke Fuchs', 'Johann Wolfgang von Goethe', 'reinekefuchs.txt')
werther1 = Text('Die Leiden des jungen Werthers 1', 'Johann Wolfgang von Goethe', 'werther1.txt')
werther2 = Text('Die Leiden des jungen Werthers 2', 'Johann Wolfgang von Goethe', 'werther2.txt')

works = [geschwister, berlichingen, iphigenie, reinekefuchs, werther1, werther2]


def analyze(text):
    text.cleanText()
    wordsAndLengths = text.longestWords()
    wordsOnly = [word[1] for word in wordsAndLengths]
    return wordsOnly


def analyzeAll(works):
    result = [analyze(work) for work in works]
    return result


final = analyzeAll(works)

for work in final:
    for word in work:
        print(word)
