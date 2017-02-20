"""
Uses the Spotify API, plus several Python libraries - Spotipy, a wrapper for the Spotify API,
and Markovify, a library for Markov chains - to pull track names of a genre from Spotify,
then use Markov chains to create random song names of a certain genre.

@author: Matt Brucker
"""

import argparse
from spotipy import Spotify
import track_text
import os.path
from numpy.random import choice

# Parse arguments
parser = argparse.ArgumentParser(description='Enter API Credentials')
parser.add_argument('--fixed', help='Generate fixed-length track', action='store_true')
parser.add_argument('genre', help='The genre of song to generate.')
args = parser.parse_args()


def save_track_list(genre):
    """
    Builds a pickle file containing the song names of up to 10,000 songs of a certain genre.
    Strips extra words after hyphens from track names, and also converts everything to lowercase.
    """
    genre_split = '+'.join(genre.split())  # Converts genre name into API-compatible string
    tracks = sp.search("genre:" + genre_split, type='track', limit=50)
    if len(tracks['tracks']['items']) == 0:  # If there were no results for this genre, raise an exception
        raise ValueError
    else:
        all_tracks = list()
        total_tracks = 0
        # Iterate until there's no more tracks, or we hit 10,000 tracks
        while tracks['tracks']['next'] and total_tracks < 10000:
            for track in tracks['tracks']['items']:
                track_name = track['name'].lower()  # Keep everything lowercase for simplicity

                # Add track name to our list of track names
                all_tracks.append(track_name)
            # Iterate to the next tracks
            tracks = sp.next(tracks['tracks'])
            total_tracks += 50

        # Stores the data to reduce the number of API calls
        file_name = 'tracks/{}.txt'.format('_'.join(genre.lower().split()))
        with open(file_name, 'w') as in_file:
            in_file.write('\n'.join(all_tracks))


def get_random_length(in_file):
    """
    Generates a random track length, in number of words.
    Works by parsing the word length of each track in in_fil, then building
    a probability distribution of lengths, and picking a length randomly
    according to that distribution.
    """
    text_lines = open(in_file, 'r').read().split('\n')
    word_lens = [len(line.split()) for line in text_lines]  # Build a list of the word length of each track
    len_freqs = [0 for val in range(0, max(word_lens))]  # Build an empty list to track probabilities
    lens = [val+1 for val in range(0, max(word_lens))]  # Build an list of possible lengths

    for length in word_lens:
        len_freqs[length-1] += 1  # Populate the probably distribution list with each track
    len_freqs = [freq/len(word_lens) for freq in len_freqs]  # Convert length counts to probabilities
    string_len = choice(lens, p=len_freqs)  # Choose a track length randomly based on the probabilities
    return string_len


def gen_random_track(genre, fixed):
    """
    Generates a random track of a given genre using Markov chains.
    """
    # Build the name of the text file to pull from
    file_name = 'tracks/{}.txt'.format('_'.join(genre.lower().split()))
    try:  # Exception handling in case the genre isn't founc
        if not os.path.isfile(file_name):
            print('Downloading list of tracks...')
            save_track_list(genre)  # Only call the API if the tracks file doesn't already exist
        with open(file_name, 'r') as in_file:
            tracks = in_file.read()  # Read the text file containing the tracks
        # Build a Markov chain from the text file
        track_len = get_random_length(file_name)
        print(track_len)
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
    sp = Spotify()
    print(gen_random_track(args.genre, args.fixed))
