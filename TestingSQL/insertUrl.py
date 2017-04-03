import sqlite3
import read_lyrics

conn = sqlite3.connect('url.db')

c = conn.cursor()

url = 'http://www.metrolyrics.com/reunited-lyrics-wutang-clan.html'
url2, listWords = read_lyrics.drawOut(url)


c.execute('SELECT * FROM urldb WHERE url=?', (url,))
if c.fetchone() == None:
    # Create table
    # Insert a row of data
    c.execute("CREATE TABLE " + url2 + " (ID Integer, Words text, Color Text)")
    c.execute("INSERT INTO urldb VALUES (?,?)", (url, 1))
    for i in range(len(listWords)):
        c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (i, listWords[i], 'NA'))

    # c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (1, 'sample text word', 'sample text color'))
    # c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (2, 'sample text word', 'sample text color'))
    # Save (commit) the changes
    conn.commit()
else:
    print('exists')
    for row in c.execute("SELECT * FROM " + url2 + " ORDER BY ID"):
        print(row)
