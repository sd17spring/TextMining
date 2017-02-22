"""
Uses the Spotify API, plus several Python libraries - Spotipy, a wrapper for the Spotify API,
and Markovify, a library for Markov chains - to pull track names of a genre from Spotify,
then use Markov chains to create random song names of a certain genre.

@author: Matt Brucker
"""

import argparse
from spotipy import Spotify
import doctest
import track_text
import os.path
from numpy.random import choice
import matplotlib
# Uncomment this line and change it if the default display backend doesn't work with matplotlib:
# matplotlib.use('GTK3Cairo')
import matplotlib.pyplot as plt


# Parse arguments
parser = argparse.ArgumentParser(description='Enter API Credentials')
parser.add_argument('--fixed', help='Generate fixed-length track', action='store_true')
parser.add_argument('--graph', help='Show a histogram of track lengths', action='store_true')
parser.add_argument('genre', help='The genre of song to generate.')
args = parser.parse_args()


def save_track_list(client, genre):
    """
    Builds a pickle file containing the song names of up to 10,000 songs of a certain genre.
    Strips extra words after hyphens from track names, and also converts everything to lowercase.
    """
    tracks = get_all_tracks(client, genre)
    # Stores the data to reduce the number of API calls
    file_name = '{}.txt'.format('_'.join(genre.lower().split()))
    with open(file_name, 'w') as in_file:
        in_file.write('\n'.join(tracks))


def get_all_tracks(client, genre, lim=10000):
    """
    Returns a list of up to lim number of track names of a particular genre.
    """
    genre_split = '+'.join(genre.split())  # Converts genre name into API-compatible string
    tracks = client.search("genre:" + genre_split, type='track', limit=50)
    if len(tracks['tracks']['items']) == 0:  # If there were no results for this genre, raise an exception
        raise ValueError
    else:
        all_tracks = list()
        total_tracks = 0
        # Iterate until there's no more tracks, or we hit 10,000 tracks
        while tracks['tracks']['next'] and total_tracks < lim:
            for track in tracks['tracks']['items']:
                track_name = track['name'].lower()  # Keep everything lowercase for simplicity
                # Add track name to our list of track names
                all_tracks.append(track_name)
            # Iterate to the next tracks
            tracks = sp.next(tracks['tracks'])
            total_tracks += 50
    return all_tracks


def get_prob_dist(vals):
    """
    Returns a probability distribution based on a list of integer values.
    The probability is a tuple of values and corresponding probabilities
    >>> get_prob_dist([1,2,4,4])
    ([1, 2, 3, 4], [0.25, 0.25, 0.0, 0.5])
    >>> get_prob_dist([1,3,5,7])
    ([1, 2, 3, 4, 5, 6, 7], [0.25, 0.0, 0.25, 0.0, 0.25, 0.0, 0.25])
    """
    val_freqs = [0 for val in range(0, max(vals))]  # Build an empty list of values
    all_vals = [val+1 for val in range(0, max(vals))]  # Build the list of values that corresponds to frequencies
    for value in vals:
        val_freqs[value-1] += 1
    val_freqs = [freq/len(vals) for freq in val_freqs]  # Convert frequencies to probabilities
    return (all_vals, val_freqs)


def get_random_length(genre, graph):
    """
    Generates a random track length, in number of words.
    Works by parsing the word length of each track in in_fil, then building
    a probability distribution of lengths, and picking a length randomly
    according to that distribution.
    """
    in_file = '{}.txt'.format('_'.join(genre.lower().split()))
    text_lines = open(in_file, 'r').read().split('\n')
    word_lens = [len(line.split()) for line in text_lines]  # Build a list of the word length of each track

    lens = get_prob_dist(word_lens)[0]  # Get the list of track lengths
    len_freqs = get_prob_dist(word_lens)[1]  # Get the probability distribution of track lengths

    string_len = choice(lens, p=len_freqs)  # Choose a track length randomly based on the probabilities
    if graph:  # If selected, display a histogram of track length frequency
        plt.hist(word_lens, bins=lens, normed=True, color='blue')
        plt.xlabel('Track name length in words')
        plt.ylabel('Probability of occurrence')
        plt.title(genre + ' Track Name Lengths')
        plt.xticks(lens)
        plt.show()
    return string_len


def gen_random_track(client, genre, fixed, graph=False):
    """
    Generates a random track of a given genre using Markov chains.
    """
    # Build the name of the text file to pull from
    file_name = '{}.txt'.format('_'.join(genre.lower().split()))
    try:  # Exception handling in case the genre isn't founc
        if not os.path.isfile(file_name):
            print('Downloading list of tracks...')
            save_track_list(client, genre)  # Only call the API if the tracks file doesn't already exist
        with open(file_name, 'r') as in_file:
            tracks = in_file.read()  # Read the text file containing the tracks
        # Build a Markov chain from the text file
        track_len = get_random_length(genre, graph)
        text_model = track_text.TrackText(tracks, state_size=1)
        # Create new randomly-generated sentence.
        if fixed:  # If the length is fixed, make a fixed-length track
            track_name = text_model.make_fixed_length(track_len, tries=20)
        else:  # make a track of any length
            track_name = text_model.make_sentence(tries=20)
        # Convert the sentence to uppercase.
        sentence = ' '.join([word[0].upper() + word[1:] for word in track_name.split()])
        return sentence
    except ValueError:
        print('Could not find any tracks from that genre.  Try again.')


if __name__ == '__main__':
    # Create spotify client and generate tracks
    doctest.testmod()
    sp = Spotify()
    print(gen_random_track(sp, args.genre, args.fixed, args.graph))
