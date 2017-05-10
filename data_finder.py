import twitter
import pickle
#who do you want to mimic
def data_finder(user_handle):
    while True:
        #data finder prompst the user to input login material
        print ('consumer_key:')
        c_k = input()
        print ('consumer_secret:')
        c_s = input()
        print ('access_token_key:')
        a_t_k = input()
        print ('access_token_secret:')
        a_t_s = input()
        #data fider uses these to login
        c_k='9x533EajbtyDTjtwAsxYHc1tZ'
        c_s='Fq13eEj8HF6xSHWUrrq8XvOshiOG0M1g7ibVpwpEgAH1UqPKQR'
        a_t_k='834076435421786112-SFdne8UH0j5vVKrJWdNzjyMuBeCIQAA'
        a_t_s='giFPH6ahXIKQJmWIOZmZRPwD1KOmqHpTUDfb3foD72Xw8'

        api = twitter.Api(consumer_key=c_k,
                          consumer_secret=c_s,
                          access_token_key=a_t_k,
                          access_token_secret=a_t_s)

        # test to see if this brings an error if it doesnt break! if it does,
        #try autenticating again
        try:
            api.VerifyCredentials()
            break
        except twitter.error.TwitterError as e:
            print(e)
            data_finder(user_handle)

    # how do i make a list of lists of words from each tweet?
    # How do i set up a login error that brings people back to the login option and works for more people than just me
    # How do i save that list so i can open it in another progam


    statuses = api.GetUserTimeline(screen_name=user_handle, count=850)
    statuses = [s.text for s in statuses]
    #print (statuses)
    words = []
    for status in statuses:
        tweet = [status.split()]
        words = words +  tweet
    statuses = words
    return statuses




if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    data_finder('pontifex')
