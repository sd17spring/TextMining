import wikipedia
import string
import unittest

class Text():

    def __init__(self):
        self.presidents = [
            'George Washington',
            'John Adams',
            'Thomas Jefferson',
            'James Madison',
            'James Monroe',
            'John Quincy Adams',
            'Andrew Jackson',
            'Martin Van Buren',
            'William Henry Harrison',
            'John Tyler',
            'James K. Polk',
            'Zachary Taylor',
            'Millard Fillmore',
            'Franklin Pierce',
            'James Buchanan',
            'Abraham Lincoln',
            'Andrew Johnson',
            'Ulysses S. Grant',
            'Rutherford B. Hayes',
            'James A. Garfield',
            'Chester Arthur',
            'Grover Cleveland',
            'Benjamin Harrison',
            'William McKinley',
            'Theodore Roosevelt',
            'William Howard Taft',
            'Woodrow Wilson',
            'Warren G. Harding',
            'Calvin Coolidge',
            'Herbert Hoover',
            'Franklin D. Roosevelt',
            'Harry S. Truman',
            'Dwight D. Eisenhower',
            'John F. Kennedy',
            'Lyndon B. Johnson',
            'Richard Nixon',
            'Gerald Ford',
            'Jimmy Carter',
            'Ronald Reagan',
            'George H. W. Bush',
            'Bill Clinton',
            'George W. Bush',
            'Barack Obama',
            'Donald Trump']

        self.blacklist = ['george', 'washington', 'adams', 'thomas', 'washingtons',
        'jefferson', 'madison', 'james', 'monroe', 'quincy', 'jacksons',
        'adams', 'andrew', 'jackson','martin', 'buren', 'tylers',
        'henry', 'harrison', 'tyler', 'polk', 'zachary', 'polks', 'taylors',
        'taylor', 'millard', 'fillmore', 'pierce', 'fillmores', 'pierces',
        'buchanan', 'abraham', 'lincoln', 'andrew', 'johnson', 'ulysses',
        'grant','rutherford', 'hayes', 'garfield', 'chester', 'johnsons',
        'arthur','grover', 'cleveland', 'benjamin', 'harrison', 'william',
        'mckinley','theodore', 'roosevelt','howard', 'grants', 'hayess',
        'woodrow', 'wilson','warren', 'harding', 'calvin', 'coolidge',
        'herbert', 'hoover','franklin', 'harry', 'truman','dwight','arthurs'
        'eisenhower', 'kennedy', 'Lyndon', 'Johnson', 'richard', 'nixon',
        'gerald', 'ford','jimmy', 'carter', 'ronald', 'reagan', 'clevelands',
        'bill', 'clinton', 'barack', 'obama', 'donald', 'trump', 'trumps',
        'president', 'william', 'would', 'which', 'years', 'zachary', 'presidential',
        'though', 'while', 'because', 'harrisons', 'mckinleys', 'hardings',
        'eisenhowers', 'kennedys', 'johnsons', 'carters', 'reagans', 'clintons',
        'state', 'states', 'wilsons', 'after', 'trumans', 'roosevelts', 'garfields',
        'coolidges', 'burens', 'lincolns', 'buchanans', 'nixons', 'fords', 'during',
        'their', 'united', 'house', 'later', 'american', 'republican', 'jeffersons'
        ]

    def load_file(self, filename):
        """ Opens each file and saves the text in a list. """

        # Open the file and store it as text
        with open(filename, 'r') as f:
            text = [line for line in f]

        return text

    def to_words(self, text):
        """ Takes a President text and splits into individual words. """
        split_words = []

        for line in text:
            split = line.split()
            split_words.extend(split)

        return split_words

    def remove_punctuation_and_whitespace(self, word):
        """ Excludes characters classified as punctuation and whitespace. """
        letters = [
            letter.lower() for letter in word
            if letter not in string.punctuation
            and letter not in string.whitespace]

        return ''.join(letters) # Join list of letters into a string

    def most_frequent(self, words, blacklist):
        """This function will take all words from the Wikipedia pages and return
            the most frequent from each page, with certain exclusions. """

        counts = {}
        for word in words:
            long_enough = len(word) >= 5
            whitelisted = word not in blacklist

            if long_enough and whitelisted:
                counts[word] = counts.get(word, 0) + 1

        return max(counts, key=counts.get)

    def main(self):
        most_common_words = []

        for filename in self.presidents:
            text = self.load_file(filename + '.txt')
            words = self.to_words(text)
            stripped = [
                self.remove_punctuation_and_whitespace(word) for word in words]
            mode = self.most_frequent(stripped, self.blacklist)
            most_common_words.append(mode)

        return most_common_words

class TestText(unittest.TestCase):

    def setUp(self):
        self.subject = Text()

    def test_to_words(self):
        # Arrange
        lines = ['That makes some sense.', 'What is up?']

        # Act
        result = self.subject.to_words(lines)

        # Assert
        expected = ['That', 'makes', 'some', 'sense.', 'What', 'is', 'up?']
        self.assertEqual(result, expected)

    def test_most_frequent(self):
        # Arrange
        blacklist = ['hello']
        words = [
            'then', 'then', 'then',
            'hello', 'hello', 'hello', 'hello',
            'fires', 'fires',
            'huzzah']

        # Act
        result = self.subject.most_frequent(words, blacklist)

        # Assert
        expected = 'fires'
        self.assertEqual(result, expected)

    def test_remove_punctuation_and_whitespace(self):
        # Arrange
        word = 'W,h!At\'\n '
        # Act
        result = self.subject.remove_punctuation_and_whitespace(word)

        # Assert
        expected = 'what'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    t = Text()
    print(t.main())
    unittest.main()
