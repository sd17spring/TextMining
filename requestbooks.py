'''
    DESC: Python script to pull specified books from the web and save them as
    .txt files for a text mining project
    AUTH: Connor Novak
    MAIL: connor@students.olin.edu
    '''
import requests
import os.path


# Make dictionary and add all books to request from Project Gutenberg
links = {'oliver_twist':'http://www.gutenberg.org/cache/epub/730/pg730.txt',
'bleak_house':'http://www.gutenberg.org/cache/epub/1023/pg1023.txt',
'great_expectations':'http://www.gutenberg.org/files/1400/1400-0.txt',
'a_christmas_carol':'http://www.gutenberg.org/files/24022/24022-0.txt',
'the_old_curiosity_shop':'http://www.gutenberg.org/files/700/700-0.txt',
'picture_of_dorian_gray':'http://www.gutenberg.org/cache/epub/174/pg174.txt',
'pride_and_prejudice':'http://www.gutenberg.org/cache/epub/42671/pg42671.txt'}


def request_book(book):
    '''
        DESC: Retrieves book from Project Gutenberg if the book isn't already
        retrieved
        ARGS:
        book - string - title of book/file to save book under
        RTRN: none
        SHOW: new file with book text
        '''
    filepath = book+'.txt'
    if (os.path.isfile(filepath)):
        print('ERR: '+filepath + ' already exists in current directory!')
    else:
        file = open(filepath, 'w')
        text = requests.get(links[key]).text
        file.write(text)
        file.close()
        print('MSG: successfully downloaded text to '+filepath+'.')


for key in links:
    print('MSG: requesting book: '+key)
    request_book(key)
