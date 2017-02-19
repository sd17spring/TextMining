"""
Uses the Spotify API, plus several Python libraries - Spotipy, a wrapper for the Spotify API,
and Markovify, a library for Markov chains - to pull track names of a genre from Spotify,
then use Markov chains to create random song names of a certain genre.

@author: Matt Brucker
"""

import argparse
import pickle
from spotipy import Spotify, oauth2
import markovify
import os.path

parser = argparse.ArgumentParser(description='Enter API Credentials')
parser.add_argument('--id', help='Your client ID.')
parser.add_argument('--secret', help='Your client secret.')
args = parser.parse_args()

token = oauth2.SpotifyClientCredentials(client_id=args.id, client_secret=args.secret)
sp = Spotify(client_credentials_manager=token)


def save_all_playlists():
    spotify_lists = sp.user_playlists('spotify')
    all_lists = list()
    while spotify_lists['next']:
        all_lists.extend(spotify_lists['items'])
        spotify_lists = sp.next(spotify_lists)
    print(all_lists[0])
    pickle.dump(all_lists, open('playlist_data.pickle', 'wb'))


def save_track_list(genre):
    genre_split = '+'.join(genre.split())  # Converts genre name into API-compatible string
    tracks = sp.search("genre:" + genre_split, type='track', limit=50)
    all_tracks = list()
    total_tracks = 0
    # Iterate until there's no more tracks, or we hit 10,000 tracks
    while tracks['tracks']['next'] and total_tracks < 10000:
        for track in tracks['tracks']['items']:
            track_name = track['name'].lower()  # Keep everything lowercase for simplicity

            #  cuts off at hyphens - this is because a lot of tracks have "live" in their name, and we don't want that
            cutoff_index = track_name.find('-')
            if cutoff_index >= 0:
                track_name = track_name[:cutoff_index]

            # Add track name to our list of track names
            all_tracks.append(track_name)
        # Iterate to the next tracks
        tracks = sp.next(tracks['tracks'])
        total_tracks += 50
    # Pickles the data to reduce the number of API calls
    pickle_name = '_'.join(genre.lower().split()) + '.pickle'
    pickle.dump(all_tracks, open(pickle_name, 'wb'))


def get_all_tracks(genre):
    file_name = '_'.join(genre.lower().split()) + '.pickle'
    if not os.path.isfile(file_name):
        save_track_list(genre)
    tracks = pickle.load(open(file_name, 'rb'))
    tracks_combined = '. '.join(tracks)
    text_model = markovify.Text(tracks_combined)




if __name__ == '__main__':
    # save_all_playlists()
    # get_all_playlists()
    # get_new_releases()
    get_all_tracks("Indie Rock")
