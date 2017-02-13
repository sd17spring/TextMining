import argparse
from spotipy import Spotify, oauth2

parser = argparse.ArgumentParser(description='Enger API Credentials')
parser.add_argument('--id', help='Your client ID.')
parser.add_argument('--secret', help='Your client secret.')
args = parser.parse_args()

token = oauth2.SpotifyClientCredentials(client_id=args.id, client_secret=args.secret)
sp = Spotify(client_credentials_manager=token)


def get_new_releases():
    res = sp.categories(limit=50)
    [print(item['name']) for item in res['categories']['items']]
    # res = sp.search(q='weezer', type='artist', limit=20)
    # print([artists for artists in res['artists']['items']])


if __name__ == '__main__':
    get_new_releases()
