import sys, praw#, requests
#import requests.auth
sys.path.insert(0, '../')
import secrets

# client_auth = requests.auth.HTTPBasicAuth(secrets.puScript, secrets.secret)
# post_data = {"grant_type": "password", "username":secrets.un, "password":secrets.pw}
# headers = {"User-Agent":"ChangeMeClient/0.1 by testProgram"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# print(response.json())

reddit = praw.Reddit(user_agent='text_mining', client_id=secrets.puScript, client_secret=secrets.secret)

sub = reddit.subreddit('magicTCG').hot(limit=5)
print([str(x) for x in sub])
