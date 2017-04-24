"""
Sarah Barden
This script is the final processing for my text mining project.  It initializes
seven different works by Goethe as Text objects (see classText.py) and finds
the top three longest words in each.
"""

from classText import Text

geschwister = Text('Die Geschwister', 'Johann Wolfgang von Goethe', 'geschwister.txt')
berlichingen = Text('Götz von Berlichingen', 'Johann Wolfgang von Goethe', 'berlichingen.txt')
iphigenie = Text('Iphigenie auf Tauris', 'Johann Wolfgang von Goethe', 'iphigenie.txt')
reinekefuchs = Text('Reineke Fuchs', 'Johann Wolfgang von Goethe', 'reinekefuchs.txt')
werther1 = Text('Die Leiden des jungen Werthers 1', 'Johann Wolfgang von Goethe', 'werther1.txt')
werther2 = Text('Die Leiden des jungen Werthers 2', 'Johann Wolfgang von Goethe', 'werther2.txt')

works = [geschwister, berlichingen, iphigenie, reinekefuchs,
         werther1, werther2]


def analyze(text):
    """
    Find the longest three words in a single text.  Takes a Text object as input
    and outputs a list of words and their lengths.
    """
    wordsAndLengths = text.longestWords(3)
    print("analyzed", wordsAndLengths)
    wordsOnly = [word[1] for word in wordsAndLengths]
    return wordsOnly


def analyzeAll(works):
    """
    Finds the longest three words for each work in a list of multiple works.
    Takes in a list of Text objects and outputs a list of words and their lengths.
    """
    result = [analyze(work) for work in works]
    return result


# running full analysis on all seven works initialized above. Prints each word
# in the console.
final = analyzeAll(works)
for work in final:
    for word in work:
        print(word)
