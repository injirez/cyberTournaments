import psycopg2
from datetime import datetime

con = psycopg2.connect(
					host = 'localhost',
					database = 'tournamentsdb',
					port = '5432',
					user = 'rodionibragimov',
					password = '3470')
cur = con.cursor()

cur.execute('insert into testt_dota (id, "tournamentTitle", "tournamentType", "tournamentDate") values (%s, %s, %s, %s)', (0, 'Test', 'Test', 'datetime.now()'))

con.commit()

cur.close()
con.close()
