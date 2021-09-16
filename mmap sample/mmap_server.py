import mmap
from contextlib import contextmanager


@contextmanager
def mmap_context(file):
    mm = mmap.mmap(fileno=file.fileno(), length=1024, access=mmap.ACCESS_WRITE)
    try:
        yield mm
    finally:
        mm.close()


def write_to_mem(file, share_data):
    with mmap_context(file) as mem:
        # mem.seek(100)
        # mem.write(share_data.encode())
        # mem.write('\x00'.encode() * (1024 - len(share_data.encode())))
        mem[10:10+len(share_data)]=share_data.encode()
        mem.flush()


if __name__ == '__main__':
    # Create a malloc
    with open('data.dat', 'w') as f:
        f.write('\x00' * 1024)

    file = open('data.dat', 'r+')
    write_to_mem(file, 'hello')
