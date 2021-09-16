from timeit import timeit
from time import sleep


def hello():
    for _ in range(1000):
        #print(_)
        sleep(0.01)


if __name__ == '__main__':
    print('start calculate')
    print("Total run time: {}" .format(timeit('hello()', setup='from __main__ import hello', number=1)))
    print('stop')
