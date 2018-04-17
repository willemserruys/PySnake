
import pymysql



class DataBaseConnection():
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='oot', passwd='root', db='dbo')
            self.cur = self.conn.cursor()
            self.connectionMade  = True
            print('connection ok')
        except:
            self.connectionMade = False
            print('Error in connection, highscores are not updated')

    def SetHighScore(self,player,score):
        if self.connectionMade:
            sql = "call dbo.InsertHighScore(%s,%s)"
            self.cur.execute(sql,(player,score))
            self.conn.commit()
    
    def GetHighScores(self):
        if self.connectionMade:
            sql = "SELECT  HGH_PlayerName,HGH_Score,cast(HGH_Date as char) FROM dbo.tblhighscore ORDER BY HGH_Score DESC LIMIT 10;"
            self.cur.execute(sql)
            return self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()