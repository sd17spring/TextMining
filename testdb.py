import sqlite3
import insertUrl
import read_lyrics
# conn = sqlite3.connect('url.db')
#
# c = conn.cursor()
# Create table
# c.execute('''CREATE TABLE urldb
#              (url text, visited INTEGER)''')
mydb = insertUrl.databaseConnect("url.db")
title = read_lyrics.drawOutTitle('http://www.metrolyrics.com/humble-lyrics-kendrick-lamar.html')
print(type(mydb.getAllValues(title)[0]))
# for row in c.execute('SELECT * FROM urldb'):
#      print(row)
# Insert a row of data

# Save (commit) the changes
# conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# conn.close()
