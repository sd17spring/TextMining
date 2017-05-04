"""
This is a self directional project with guidance from the Software Design
teaching team.

@author: Colvin Chapman
"""

import requests


def write_book(URL, name_file):
    body = requests.get(URL).text
    cooldict = open(name_file, 'w')
    cooldict.write(body)
    cooldict.close()


write_book("http://www.gutenberg.org/cache/epub/730/pg730.txt", "Oliver_Twist")
write_book("http://www.gutenberg.org/files/766/766-0.txt", "David_Copperfield")
write_book("http://www.gutenberg.org/cache/epub/1661/pg1661.txt",
           "Sherlock_Holmes")


"""
the length of webster is 28,930,471 characters
the english language has about 129,000 words"""
