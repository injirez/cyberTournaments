# import psycopg2
# from datetime import datetime

# con = psycopg2.connect(
# 					host = 'localhost',
# 					database = 'tournamentdb',
# 					port = '5433',
# 					user = 'rodionibragimov',
# 					password = 'password')
# cur = con.cursor()

# cur.execute('insert into testt_dota (id, "tournamentTitle", "tournamentType", "tournamentDate") values (%s, %s, %s, %s)', (1, 'TI21', '1v1 MID', datetime.now()))

# con.commit()

# cur.close()
# con.close()
grid =[['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]

for i in range(1,100):

	for i in range(len(grid[0])):
	    for j in range(len(grid)):
	        print(grid[j][i], end='')
	    print()