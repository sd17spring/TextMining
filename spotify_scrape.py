"""
Uses the Spotify API, plus several Python libraries - Spotipy, a wrapper for the Spotify API,
and Markovify, a library for Markov chains - to pull track names of a genre from Spotify,
then use Markov chains to create random song names of a certain genre.

@author: Matt Brucker
"""

import argparse
from spotipy import Spotify, oauth2
import markovify
import os.path

parser = argparse.ArgumentParser(description='Enter API Credentials')
parser.add_argument('--id', help='Your client ID.')
parser.add_argument('--secret', help='Your client secret.')
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
        punctuation = '&()\"[]:'  # Used to remove random punctuation from songs
        # Iterate until there's no more tracks, or we hit 10,000 tracks
        while tracks['tracks']['next'] and total_tracks < 10000:
            for track in tracks['tracks']['items']:
                track_name = ''.join([char for char in track['name'].lower() if char not in punctuation])  # Keep everything lowercase for simplicity
                #  cuts off at hyphens - this is because a lot of tracks have "live" in their name, and we don't want that
                cutoff_index = track_name.find('-')
                if cutoff_index >= 0:
                    track_name = track_name[:cutoff_index]

                # Add track name to our list of track names
                all_tracks.append(track_name)
            # Iterate to the next tracks
            tracks = sp.next(tracks['tracks'])
            total_tracks += 50

        # Stores the data to reduce the number of API calls
        file_name = 'tracks/{}.txt'.format('_'.join(genre.lower().split()))
        with open(file_name, 'w') as in_file:
            in_file.write('\n'.join(all_tracks))


def gen_random_track(genre):
    """
    Generates a random track of a given genre using Markov chains.
    """
    # Build the name of the text file to pull from
    file_name = 'tracks/{}.txt'.format('_'.join(genre.lower().split()))
    try:  # Exception handling in case the genre isn't founc
        if not os.path.isfile(file_name):
            save_track_list(genre)  # Only call the API if the tracks file doesn't already exist
        with open(file_name, 'r') as in_file:
            tracks = in_file.read()  # Read the text file containing the tracks
        # Build a Markov chain from the text file
        text_model = markovify.NewlineText(tracks, state_size=1)
        # Create new randomly-generated sentence and convert to uppercase
        sentence = ' '.join([word[0].upper() + word[1:] for word in text_model.make_short_sentence(140).split()])
        print(sentence)
    except ValueError:
        print('Could not find any tracks from that genre.  Try again.')


if __name__ == '__main__':
    # Handle Spotify client authorization
    if args.id and args.secret:
        token = oauth2.SpotifyClientCredentials(client_id=args.id, client_secret=args.secret)
    else:
        in_file = open('creds.txt', 'r').read().split()
        client_id = in_file[0]
        client_secret = in_file[1]
        token = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = Spotify(client_credentials_manager=token)

    gen_random_track(args.genre)
