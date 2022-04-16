import psycopg2 # postgres-sql library

# Connect db
conn = psycopg2.connect(
            host='localhost',
            database='test',
            user='postgres',
            password=1234,
            port=5432
)


cur = conn.cursor()
cur.execute('SELECT * from company')
for query in cur.fetchall():
    print(query)
cur.close()
