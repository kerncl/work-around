import lmdb

env = lmdb.open('./db', map_size=2e-9, max_dbs=1)
db1 = env.open_db('db1'.encode())
txn = env.begin(write=True)

# Wrote top level of db
txn.put(key='1'.encode(), value='aaa'.encode())
txn.put(key='2'.encode(), value='bbb'.encode())
txn.put(key='3'.encode(), value='ccc'.encode())

txn.delete(key='1'.encode())

txn.put(key='3'.encode(), value='ddd'.encode())


## Wrote internal db: db1
txn.put(key=b'internal_1', value=b'internal_aaaa', db=db1)
txn.put(key=b'internal_2', value=b'internal_bbbb', db=db1)

txn.commit()
env.close()