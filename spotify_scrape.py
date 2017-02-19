import argparse
import pickle
import re
from spotipy import Spotify, oauth2
import markovify

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


def get_all_playlists():
    lists = pickle.load(open('playlist_data.pickle', 'rb'))
    all_names = [play['name'] for play in lists if not re.match(play['name'],'Top')]
    names_new = ' '.join(all_names)
    text_model = markovify.Text(names_new)

    print(text_model.make_sentence())
    # keywords = dict()
    # for playlist in lists:
    #     keys = playlist['name'].split()
    #     for key in keys:
    #         if key not in keywords:
    #             keywords[key] = 1
    #         else:
    #             keywords[key] += 1
    # [print(key, ': ', keywords[key]) for key in keywords if keywords[key] > 40]


def get_new_releases():
    res = sp.search('Indie', type='track')
    print(res)
    # res = sp.categories(limit=50)
    # print (res)
    # cat_id = [item['id'] for item in res['categories']['items'] if item['name'] == 'Indie'][0]
    # play = sp.category_playlists(category_id=cat_id)
    # new_list = play['playlists']['items'][0]
    # num_lists = 0
    # lists = sp.user_playlists('spotify')
    # print(lists)
    # while lists['next']:
    #     num_lists += 50
    #     lists = sp.next(lists)
    # print(str(num_lists))
    # [print(new_list[item]) for item in new_list]
    # res = sp.search(q='weezer', type='artist', limit=20)
    # print([artists for artists in res['artists']['items']])


if __name__ == '__main__':
    # save_all_playlists()
    get_all_playlists()
    # get_new_releases()
