import wikipedia
import string

def read_presidents_texts():
    presidents = ['George Washington', 'John Adams', 'Thomas Jefferson',
    'James Madison', 'James Monroe', 'John Quincy Adams', 'Andrew Jackson',
    'Martin Van Buren', 'William Henry Harrison', 'John Tyler',
    'James K. Polk', 'Zachary Taylor', 'Millard Fillmore', 'Franklin Pierce',
    'James Buchanan', 'Abraham Lincoln', 'Andrew Johnson', 'Ulysses S. Grant',
    'Rutherford B. Hayes', 'James A. Garfield', 'Chester Arthur',
    'Grover Cleveland', 'Benjamin Harrison', 'William McKinley',
    'Theodore Roosevelt', 'William Howard Taft', 'Woodrow Wilson',
    'Warren G. Harding', 'Calvin Coolidge', 'Herbert Hoover',
    'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower',
    'John F. Kennedy', 'Lyndon B. Johnson', 'Richard Nixon', 'Gerald Ford',
    'Jimmy Carter', 'Ronald Reagan', 'George H. W. Bush', 'Bill Clinton',
    'George W. Bush', 'Barack Obama', 'Donald Trump'
    ]
    for name in presidents:
        with open(name + '.txt', 'r') as f:
            words = make_words(f.readlines())
            formatted_words = format_words(words)
            frequencies = word_frequency(formatted_words)
            print(name)
            print(frequencies)


def make_words(president_file_lines):
    """ This function takes each President file and splits the lines into words.
        >>> make_words(['What do you mean?'])
        ['What', 'do', 'you', 'mean?']
    """
    split_words = []
    for string in president_file_lines:
        split = string.split()
        split_words.extend(split)
    return split_words


def exclude(letter):
    """This function should exclude characters that are punctuation or
    whitespace.
    >>> exclude(' ')
    True
    >>> exclude('#')
    True
    """
    return letter in string.punctuation or letter in string.whitespace


def format_word(word):
    """This function will strip all of the words of punctuation and whitespaces
        then make the words lowercase.
        >>> format_word('DOG')
        'dog'
        >>> format_word('!!!')
        ''
    """
    return ''.join(letter for letter in word if not exclude(letter)).lower()


def format_words(words):
    """This function should run all of the words from the Wikipedia pages through
        format_word function and return a list of the formatted words.
        >>> format_words(['D!oG', 'what', 'CELLAR'])
        ['dog', 'what', 'cellar']
    """
    formatted_words = []
    for word in words:
        better_word = format_word(word)
        formatted_words.append(better_word)
    return formatted_words


def word_frequency(formatted_words):
    """This function will take all words from the Wikipedia pages and return
        the most frequent from each page, with certain exclusions.
        >>> word_frequency(['dogs', 'cat', 'the', 'fires', 'fires'])
        'fires'
        >>> word_frequency(['tetris', 'tetris', 'and', 'but'])
        'tetris'
    """
    d = {}
    for word in formatted_words:
        with open('bad_words.txt', 'r') as f:
            for line in f:
                if word in line:
                    continue
                elif len(word) < 5:
                    continue
                else:
                    count = d.get(word, 0) + 1
                    d[word] = count
                    maximum_frequency = max(d.values())
                    word_frequencies = lookup(d, maximum_frequency)
    return word_frequencies


def lookup(d, v):
    """This function should take a value and search for its corresponding key in
        the dictionary.
        >>> d = {'dog' : 5}
        >>> lookup(d, 5)
        'dog'
    """
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    read_presidents_texts()
