"""
This is a self directional project with guidance from the Software Design
teaching team.

@author: Colvin Chapman
"""

import requests
import pickle

unabridged_webster = requests.get(
     'http://www.gutenberg.org/cache/epub/29765/pg29765.txt').text

'''I attempted to do some pickling, but in the interest of time, left this as
 unfinished business:

pickle.dump('Webster_Dictionary', unabridged_webster,)
    '''


def test_writing():
    """Hey, it made a file!
        """
    test = open('test.txt', 'w')
    test.write('This should appear in a text file somewhere!')
    test.close()
    return


def write_dictionary():
    cooldict = open('Webster.txt', 'w')
    cooldict.write(unabridged_webster)
    cooldict.close()


write_dictionary()

print(len(unabridged_webster))
# print(unabridged_webster[0: 3000])

"the length of webster is 28,930,471 characters"
"the english language has about 129,000 words"
