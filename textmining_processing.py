import pickle
from classText import Text
"""
Finding  the longest word
"""

def final_analysis(text):
    clean = clean_text(text)
    top = longest_words(clean)
    for pair in top:
        print(pair)


# final_analysis('berlichingen.txt')
final_analysis('geschwister.txt')
# final_analysis('iphigenie.txt')
# final_analysis('reinekefuchs.txt')
# final_analysis('werther1.txt')
# final_analysis('werther2.txt')
