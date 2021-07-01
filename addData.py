import psycopg2
from datetime import datetime

con = psycopg2.connect(
    host='localhost',
    database='cybertournaments',
    port='5432',
    user='rodionibragimov',
    password='3470')
cur = con.cursor()

def addData(title, status, startTime, gameMode, participant, reward, siteName, link, img):
    cur.execute(
        'insert into "Dota_dota" ("title", "status", "startTime", "gameMode", "participant", "reward", "siteName", "link", "dateTime", "img") values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (title, status, startTime, gameMode, participant, reward,
         siteName, link,
         datetime.now(), img))

    con.commit()

    cur.close()
    con.close()
