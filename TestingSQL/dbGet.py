import sqlite3
conn = sqlite3.connect('url.db')

c = conn.cursor()

url = 'http://www.metrolyrics.com/colors-of-the-wind-lyrics-disney.html'

url2 = "colorsofthewind"
c.execute('SELECT * FROM urldb WHERE url=?', (url,))
if c.fetchone() == None:
    # Create table
    # Insert a row of data
    c.execute("CREATE TABLE " + url2 + " (ID Integer, Words text, Color Text)")
    c.execute("INSERT INTO urldb VALUES (?,?)", (url, 1))
    c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (1, 'sample text word', 'sample text color'))
    c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (2, 'sample text word', 'sample text color'))
    # Save (commit) the changes
    conn.commit()
else:
    print('exists')
    for row in c.execute("SELECT * FROM " + url2 + " ORDER BY ID"):
        print(row)

# Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# conn.commit()
# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)
