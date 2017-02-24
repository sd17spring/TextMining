import requests
import pickle

# Save data to a file (will be part of your data fetching script)
odyssey = requests.get('https://www.gutenberg.org/files/48895/48895-0.txt').text
a = open('odyssey.pickle', 'wb')
pickle.dump(odyssey, a)
a.close()

iliad = requests.get('http://www.gutenberg.org/cache/epub/6130/pg6130.txt').text
a0 = open('iliad.pickle', 'wb')
pickle.dump(iliad, a0)
a0.close()


bible = requests.get('http://www.gutenberg.org/cache/epub/30/pg30.txt').text
b = open('bible.pickle', 'wb')
pickle.dump(bible, b)
b.close()

cant = requests.get('http://www.gutenberg.org/cache/epub/2383/pg2383.txt').text
c = open('cant.pickle', 'wb')
pickle.dump(cant, c)
c.close()

shakes = requests.get('http://www.gutenberg.org/cache/epub/2243/pg2243.txt').text
d = open('shakes.pickle', 'wb')
pickle.dump(shakes, d)
d.close()

don = requests.get('http://www.gutenberg.org/cache/epub/996/pg996.txt').text
d0 = open('don.pickle', 'wb')
pickle.dump(don, d0)
d0.close()

pride = requests.get('http://www.gutenberg.org/files/1342/1342-0.txt').text
e = open('pride.pickle', 'wb')
pickle.dump(pride, e)
e.close()

frank = requests.get('http://www.gutenberg.org/cache/epub/84/pg84.txt').text
e0 = open('frank.pickle', 'wb')
pickle.dump(frank, e0)
e0.close()

alice = requests.get('http://www.gutenberg.org/files/11/11-0.txt').text
f = open('alice.pickle', 'wb')
pickle.dump(alice, f)
f.close()

sherlock = requests.get('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').text
g = open('sherlock.pickle', 'wb')
pickle.dump(sherlock, g)
g.close()

wilde = requests.get('http://www.gutenberg.org/cache/epub/844/pg844.txt').text
g0 = open('wilde.pickle', 'wb')
pickle.dump(wilde, g0)
g0.close()

#meta = requests.get('http://www.gutenberg.org/cache/epub/5200/pg5200.txt').text
#h = open('meta.pickle', 'wb')
#pickle.dump(meta, h)
#h.close()

suprise = requests.get('http://www.gutenberg.org/cache/epub/147/pg147.txt').text
i = open('suprise.pickle', 'wb')
pickle.dump(suprise, i)
i.close()
