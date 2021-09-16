import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg,signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # pretend waiting a long time for I/O
    # for _ in range(10):
    #     print('hi')
    time.sleep(10)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


if __name__ == '__main__':
    result = supervisor()
    print('Answer:', result)