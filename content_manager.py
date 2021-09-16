import os
from contextlib import contextmanager

# Write file
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('write_file.txt', 'w') as f:
    f.write('Writing a content into a file')

print(f.closed)

# Change directory
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('__pycache__'):
    print(os.listdir())

with change_dir('.idea'):
    print(os.listdir())