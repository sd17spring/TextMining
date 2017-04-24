import pickle
import requests

geschwister = requests.get('http://www.gutenberg.org/cache/epub/2406/pg2406.txt').text
f = open('geschwister.txt', 'wb')
pickle.dump(geschwister, f)
f.close()

berlichingen = requests.get('http://www.gutenberg.org/cache/epub/2321/pg2321.txt').text
f = open('berlichingen.txt', 'wb')
pickle.dump(berlichingen, f)
f.close()

reinekefuchs = requests.get('http://www.gutenberg.org/cache/epub/2228/pg2228.txt').text
f = open('reinekefuchs.txt', 'wb')
pickle.dump(reinekefuchs, f)
f.close()

iphigenie = requests.get('http://www.gutenberg.org/cache/epub/2054/pg2054.txt').text
f = open('iphigenie.txt', 'wb')
pickle.dump(iphigenie, f)
f.close()

werther1 = requests.get('http://www.gutenberg.org/cache/epub/2407/pg2407.txt').text
f = open('werther1.txt', 'wb')
pickle.dump(werther1, f)
f.close()

werther2 = requests.get('http://www.gutenberg.org/cache/epub/2408/pg2408.txt').text
f = open('werther2.txt', 'wb')
pickle.dump(werther2, f)
f.close()
