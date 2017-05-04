'''Mini Project 3: Text Mining
Software Design Spring 2017
Gracey Wilson

This script parses the text of Romeo and Juliet,
counts how often each character speaks, and returns
the percentage of lines spoken by male and female characters.'''

import string
import pickle

input_file = open('romeo_juliet_full_text.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)
list_of_words = list(reloaded_copy_of_texts.split())  # Make the words in the textfile a list of strings

char_dict = {'Chor.' : 'Mixed',
             'Samp.' : 'Male',
             'Greg.' : 'Male',
             'Abr.' : 'Male',
             'Bal.' : 'Male',
             'Ben.' : 'Male',
             'Tyb.' : 'Male',
             'Officer.' : 'Male',
             'Citizens.' : 'Mixed',
             'Cap.' : 'Male',
             'Wife.' : 'Female',
             'Cap. Wife.' : 'Female', # only 2 lines. 'Wife.' and 'Cap. Wife' are both Mrs. Cap
             'Mon.' : 'Male',
             'M. Wife.' : 'Female',
             'Prince.' : 'Male',
             'Rom.' : 'Male',
             'Par.' : 'Male',
             'Serv.' : 'Male',
             'Nurse.' : 'Female',
             'Jul.' : 'Female',
             'Mer.' : 'Male',
             'Friar.' : 'Male',
             'Laur.' : 'Male',
             'John.' : 'Male',
             'Peter.' : 'Male',
             'Apoth.' : 'Male',
             '1. Serv.' : 'Male',
             '2. Serv.' : 'Male',
             '3. Serv.' : 'Male',
             '2. Cap.' : 'Male',}


def count_character_gender(dict_name):
    '''Counts how many male and female characters there are in the play.'''
    number_of_male_characters = 0
    number_of_female_characters = 0
    for value in dict_name.values():
        if value == 'Male':
            number_of_male_characters = number_of_male_characters + 1
        elif value == 'Female':
            number_of_female_characters = number_of_female_characters + 1
    answer = 'There are ' + str(number_of_male_characters) + ' speaking male characters and ' + str(number_of_female_characters) + ' speaking female characters.'
    print(answer)


def handle_2word_chars(list_of_words):
    '''Deals with all 2-word character abbreviations in the script.
    i.e. 'M.' becomes 'M. Wife.' like it appears in the dictionary.
        NOTE: Does not account for 'Cap. Wife' (because 'Cap.' is a
        different character so the method of combining any string
        that starts with 'Cap.' with the string that comes after it
        would not increase overall accuracy.)'''
    for i in range(len(list_of_words)):
        if list_of_words[i] in ['M.', '1.', '2.', '3.']:            # if the word IS in list of words
            list_of_words[i] = list_of_words[i] + str(' ') + list_of_words[i+1]
    return list_of_words


def parse(abbr_character_name,text_file_name):
    '''Takes abbreviated character name as input (ie "Samp." for Sampson)
    Counts and returns # of times each abbreviated name appears (and
    therefore the number of times the character speaks in the text).
        NOTE: 'Cap. Wife.' and 'Wife.' are the same person but this script
        is not currently aware of that fact (which is why it thinks there
        are 5 female characters when in reality there are 4. This also
        causes discrepancies in the final calculation of the averages.)'''
    number_of_mentions = 0
    for word in text_file_name:
        if word == abbr_character_name:
            number_of_mentions = number_of_mentions + 1
    return number_of_mentions


def parse_text_for_mentions(char_dict, text_file_name):
    '''Counts number of times each key of dict_name appears in modified_text.
    Takes a dictionary that maps character name to gender and a text file (in the form of a list of strings)
    Returns name_number: a dictionary that maps character names to number of times they speak.'''
    mentions = {}
    for key in char_dict.keys():
        number_of_mentions = parse(key, text_file_name)
        mentions[key] = number_of_mentions
    return mentions


# print(name_number)         # unit test; returns dictionary with character names as keys and # of times mentioned as value


def percent_breakdown(name_number,char_dict):
    '''Calculates average number of times male and female characters speak.
    Takes 2 dictionaries as input arguments:
        1. name_number: maps character names to how many times they speak
        2. char_dict: maps character names to gender
    Creates a dictionary mapping genders to lines spoken.
    Returns percentage of lines spoken by each gender.'''

    gender_lines = {}
    for key,value in name_number.items():
        gender_lines[key] = name_number[key]
    for key,value in char_dict.items():
        gender_lines[value] = char_dict[value]

    male_lines = 0
    female_lines = 0
    for key,value in gender_lines.items:
        if key == 'Male':
            male_lines += value
        if key == 'Female':
            female_lines += value
    total_lines = male_lines + female_lines
    male_percent = (male_lines / total_lines) * 100
    female_percent = (female_lines / total_lines) * 100
    print('Male characters say '+str(male_percent)+' of the lines. Female characters say '+str(female_percent)+' of the lines.'

if __name__ == '__main__':
    count_character_gender(char_dict)
    modified_text = handle_2word_chars(list_of_words)
    name_number = dict(parse_text_for_mentions(char_dict,modified_text))
    percent_breakdown(name_number,char_dict)
