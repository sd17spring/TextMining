import sqlite3
import read_lyrics


class databaseConnect:
    def __init__(self,dbFile):
        self.conn = sqlite3.connect(dbFile)
        self.c = self.conn.cursor()

    def creatURLDB(self,url, url2, listWords):
        self.c.execute('SELECT * FROM urldb WHERE url=?', (url,))
        if self.c.fetchone() == None:
            # Create table
            # Insert a row of data
            self.c.execute("CREATE TABLE " + url2 + " (ID Integer, Words text, Color Text)")
            self.c.execute("INSERT INTO urldb VALUES (?,?)", (url, 0))
            for i in range(len(listWords)):
                self.c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (i, listWords[i], 'NA'))

            # self.c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (1, 'sample text word', 'sample text color'))
            # self.c.execute("INSERT INTO " + url2 + " VALUES (?,?,?)", (2, 'sample text word', 'sample text color'))
            # Save (commit) the changes
            self.conn.commit()
            return True
        else:
            return False

    def checkVisited(self,url):
        self.c.execute('SELECT * FROM urldb WHERE url=?', (url,))
        result = self.c.fetchone()
        if result == None:
            return None
        else:
            return result[1] == 1

    def setVisited(self,url):
        self.c.execute("UPDATE urldb SET visited =:visited WHERE url =:url", {"visited" : 1, "url": url})
        self.conn.commit()

    def getWord(self,url2, index):
        self.c.execute("SELECT * FROM " + url2 + " WHERE ID =:ID", {"ID": index})
        myWord = self.c.fetchone()
        if(myWord is not None):
            return myWord[1]
        return "Error"

    def createBase(self):
        self.c.execute('''CREATE TABLE urldb
                     (url text, visited INTEGER)''')
        self.conn.commit()

    def getColor(self,url2, index):
        self.c.execute("SELECT * FROM " + url2 + " WHERE ID =:ID", {"ID": index})
        myCol = self.c.fetchone()
        if(myCol is not None):
            return myCol[2]
        return "#000000"

    def setColor(self,url2, index, color):
        self.c.execute("UPDATE " + url2 + " SET Color =:color WHERE ID =:ID", {"color" : color, "ID": index})
        self.conn.commit()

    def getCount(self, url2):
        self.c.execute("SELECT COUNT(*) FROM " + url2);
        return self.c.fetchone()[0]

    def getAllValues(self,url2):
        allVal = []
        for row in self.c.execute('SELECT * FROM ' + url2):
             print(row)
             allVal.append(list(row))
        return allVal

# mydb = databaseConnect('url.db')
#
# url = 'http://www.metrolyrics.com/something-there-beauty-and-the-beast-lyrics-disney.html'
# listWords = read_lyrics.drawOutWords(url)
# url2 = read_lyrics.drawOutTitle(url)

# print(mydb.creatURLDB(url,url2,listWords))
# print(mydb.checkVisited(url))
# print(mydb.getWord(url2,0))
# print(mydb.getColor(url2,0))
# print(mydb.setColor(url2,0,'BLUE'))
# print(mydb.getColor(url2,0))
#
# for index in range(mydb.getCount(url2)):
#     mainword = mydb.getWord(url2,index)
#     for i in range(1, 15):
#         if(index - i < 0):
#             break
#         newWord = mydb.getWord(url2, index-i)
#         rr = read_lyrics.two_rhyme(mainword, newWord)
#         if(rr >= 150):
#             print(mainword)
#             print(newWord)
#             print(rr)
