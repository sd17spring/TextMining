import twitter
import pickle

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

def remove_stuff(statuses):
    '''
    Remove the urls and hashtags that sometimes appear at the end of the
    status messages
    Returns a list of status texts
    '''
    res = []
    for status in statuses:
        cur = status.text
        while cur.find('https:')>0:
            cur = cur[:cur.find('https:')]
        res.append(cur)
    return res

d = open('data.txt','wb')
statuses = api.GetUserTimeline(screen_name='ConanOBrien',count=10000)
part1 = remove_stuff(statuses)
statuses = api.GetUserTimeline(screen_name='kevinseccia',count=10000)
part2 = remove_stuff(statuses)
statuses = api.GetUserTimeline(screen_name='weedguy420boner',count=10000)
part3 = remove_stuff(statuses)
part1.extend(part2)
part1.extend(part3)
pickle.dump(part1,d)
d.close()
