import argparse
import lmdb
from pathlib import Path


def path_validation(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File: {path} not found")
    return str(path.absolute())


def dump_lmdb(lmdb_path:str, db:str, path:str):
    env = lmdb.open(lmdb_path, max_dbs=1)
    if db:
        db = env.open_db(db.encode())
    txn = env.begin()

    print("Start converting lmdb to csv")
    with open(path, 'w') as f:
        for k,v in txn.cursor():
            f.write(f"{k.decode()}, {v.decode()} \n")

    print('Done !!!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-lmdb', '--lmdb_path',
                        help='lmdb path',
                        type=path_validation)
    parser.add_argument('-db', '--db',
                        help='Database',
                        default=None,
                        type=str)
    parser.add_argument('-path', '--path',
                        help='csv path')
    args = parser.parse_args(['--lmdb_path', r'C:\github\AMD\pysy\pysy\config\stones\stones_a0_SP5', '--path', r'C:\temp\lmdb_test\ppr_all_nodes.csv'])
    args = vars(args)
    dump_lmdb(**args)