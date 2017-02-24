import pickle
import string
import random

input_file4 = open('hamlet.pickle', 'rb')
hamlet_reloaded = pickle.load(input_file4)
hamlet_reloaded = hamlet_reloaded[12890:-135]

input_file5 = open('sonnets.pickle', 'rb')
sonnets_reloaded = pickle.load(input_file5)
sonnets_reloaded = sonnets_reloaded[775:-19150]

input_file6 = open('petrarch.pickle', 'rb')
petrarch_reloaded = pickle.load(input_file6)
petrarch_reloaded = petrarch_reloaded[450000:-40855]

test_text = 'Hello cruel world \n Why are people cruel \n I do not love the world \n Why are we here'
bad_punctuation = '[]*()_'
good_punctuation = '.:,;!?'
prefix_length = 2


def process_file(text):
    '''basically a 'run' file. initializes the dictionaries and some variables.
    splits the text into lines and does other functions with each line only if
    the line is trivial (isn't too short to constitute a line).
    '''
    hist = dict()
    prefixes_dict = dict()
    line_hangover = []
    for line in text.splitlines():
        if len(line) > 20:
            line_hangover = process_line(line, hist, line_hangover, prefixes_dict)
    write_verse(hist, prefixes_dict)


def process_line(line, hist, extended_line, prefixes_dict):
    '''Takes a line, removes apostrophes and hyphens, and appends the frequency
    dictionary with each word. It returns the last n words of a line to be
    used with the next function for determining prefixes.
    '''
    line = line.replace('-', ' ')
    line = line.replace("'", '')
    for word in line.split():
        word = word.strip(string.whitespace)
        word = word.strip(bad_punctuation)
        if len(word) > 0:
            if word[0] not in string.digits:
                hist[word] = hist.get(word, 0) + 1
                extended_line.append(word)
    process_prefixes(extended_line, prefixes_dict)
    line_hangover = extended_line[-prefix_length:]
    return line_hangover


def process_prefixes(extended_line, prefixes_dict):
    '''takes each group of n words in the line and updates a dictionary with
    the group of n words as the key and the next word as its suffix.
    '''
    count = 0
    while count < len(extended_line)-prefix_length:
        prefix = tuple(extended_line[count:count+prefix_length])
        suffix = extended_line[count+prefix_length],
        prefixes_dict[prefix] = prefixes_dict.get(prefix, tuple()) + suffix
        count += 1


def write_verse(hist, prefixes_dict):
    '''This is the Markov Chain function. It takes the dictionary of prefixes
    and suffixes and writes a sonnet.
    '''
    new_text = ''
    prefix = list(random.choice(list(prefixes_dict.keys())))
    while prefix[0][0].islower():
        prefix = list(random.choice(list(prefixes_dict.keys())))
    line_length = 0
    line_count = 0
    while line_count < 15:
        if tuple(prefix) not in prefixes_dict.keys():
            prefix = list(random.choice(list(prefixes_dict.keys())))
        options = prefixes_dict[tuple(prefix)]
        next_word = random.choice(options)

        if line_length < 6:
            if line_length == 0:
                prefix[0] = prefix[0].title()
                new_text = new_text + prefix[0] + ' '
                line_length += 1
            else:
                new_text = new_text + prefix[0] + ' '
                line_length += 1
        else:
            if prefix[0][-1] in good_punctuation or line_length > 7:
                if line_count == 14:
                    if prefix[0][-1] in ';:,':
                        prefix[0] = prefix[0][0:-1] + '.'
                    elif prefix[0][-1] not in '.!?':
                        prefix[0] = prefix[0] + '.'
                new_text = new_text + prefix[0] + '\n'
                line_length = 0
                line_count += 1
            else:
                new_text = new_text + prefix[0] + ' '
                line_length += 1

        prefix.pop(0)
        prefix.append(next_word)
    print(new_text)


process_file(sonnets_reloaded)
