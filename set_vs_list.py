from timeit import timeit


list_num = [i for i in range(10000)] # [0,1,2,3,4 .... 10000]
list_num.pop() # pop the last number
set_num = set(list_num)


def list_iteration():
    for i in range(10000):
        if i not in list_num:
            return i


def set_iteration():
    for i in range(10000):
        if i not in set_num:
            return i


if __name__ == '__main__':
    print('set iteration')
    print(f"Runt time for set iteration: {timeit('set_iteration()', setup='from __main__ import set_iteration', number = 10)}s")
    print('List iteration')
    print(f"Run time for list iteration: {timeit('list_iteration()', setup='from __main__ import list_iteration', number = 10)}s")
