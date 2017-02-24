import pickle
import requests


if __name__ == '__main__':

    f = open('obamaWik2.pickle', 'wb')
    pickle.dump(requests.get('https://en.wikipedia.org/wiki/Barack_Obama').text, f)
    f.close
    f = open('trumpWik2.pickle', 'wb')
    pickle.dump(requests.get('https://en.wikipedia.org/wiki/Donald_Trump').text, f)
    f.close
    f = open('obamaCon.pickle', 'wb')
    pickle.dump(requests.get('http://www.conservapedia.com/Barack_Hussein_Obama').text, f)
    f.close
    f = open('trumpCon.pickle', 'wb')
    pickle.dump(requests.get('http://www.conservapedia.com/Donald_Trump').text, f)
    f.close
