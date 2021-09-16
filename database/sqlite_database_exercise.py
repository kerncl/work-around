import sqlite3

connection = sqlite3.connect('user.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS User (User_ld INT PRIMARY KEY, First_name TEXT, Last_name TEXT, Email_address TEXT) ''')

data = [('11717417', 'Chin', 'Linn Kern', 'linn.kern.chin@intel.com'),
        ('11717222', 'Lim', 'Zhi Qing', 'zhi.qing.lim@intel.com') ]

#c.executemany("INSERT INTO User VALUES (?,?,?,?)", data)

c.execute("SELECT Email_address FROM User")
print(c.fetchall())

connection.commit()
connection.close()
