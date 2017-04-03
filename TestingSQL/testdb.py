import sqlite3
conn = sqlite3.connect('url.db')

c = conn.cursor()
url = 'http://www.metrolyrics.com/retrograde-lyrics-james-blake.html'
# Create table
c.execute('''CREATE TABLE urldb
             (url text, visited INTEGER)''')

# Insert a row of data
c.execute("INSERT INTO urldb VALUES (?,?)", (url, 1))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
