from hashlib import md5
import subprocess
import os

def md5sum(fname):
    with open(fname, 'rb') as f:
        hash_md5 = md5()
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()[-8:]

if __name__ == '__main__':
    fname = 'class.py'
    print(f'Python checksum: {md5sum(fname)}')
    p = subprocess.Popen(['cd'], stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    print(f'Unix checksum: {output}')
