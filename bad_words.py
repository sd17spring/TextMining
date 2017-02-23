
def bad_words():
    list_bad_words = ['george', 'washington', 'adams', 'thomas', 'washingtons'
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
    f = open('bad_words.txt', 'w')
    for string in list_bad_words:
        f.write(string + ' ' )
    f.close()


if __name__ == '__main__':
    bad_words()
