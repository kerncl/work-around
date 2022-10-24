import lmdb

# env = lmdb.Environment('db')
env = lmdb.open('./db', max_dbs=2)
child_db = env.open_db('db1'.encode())
txn = env.begin()

print('Access top level db')
for k,v in txn.cursor():
    print(k,v)

print('Access child database: db1')
for k, v in txn.cursor(child_db):
    print(k,v)

# Get from specific db
print(txn.get('internal_1'.encode(), db=child_db))