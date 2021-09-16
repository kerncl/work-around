import sqlite3

connection = sqlite3.connect('moves.db')
cursor = connection.cursor()

### Create new table if doesnt exist ###
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

### Insert one row of data into table ###
# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
cursor.execute("SELECT * FROM Movies")
# print(cursor.fetchall())


### Insert multiple row of data into table ###
famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
               ('Back to the Future', 'Steven Spielberg', 1995),
               ('Moonrise Kingdom', 'Wes Anderson', 2012)]
# cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)
cursor.execute('SELECT * FROM Movies')
# print(cursor.fetchall())


### Print row of data in row ###
rowdata = cursor.execute('SELECT * FROM Movies')
print('Using for loop')
for data in rowdata:
    print(data)

### Select specific data ###
print('Using WHERE to select specific data needed')
release_year = (1995, )
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchone())

### Save changes and closed it ###
connection.commit()
connection.close()
