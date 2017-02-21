import twitter
import pickle

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

statuses = api.GetUserTimeline(screen_name='ConanOBrien',count=10000)
d = open('data.txt','wb')
pickle.dump(statuses,d)
d.close()
