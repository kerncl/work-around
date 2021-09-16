import threading
import time
import math

def start(n=10):
    sec_arg = 5.0
    cptr = 0
    time_started = time.time()
    time_init = time.time()
    while cptr < 100:
        cptr += 1
        time_start = time.time()
        sleep_sec = ((time_init + (sec_arg * cptr)) - time_start)
        print(f"sleep time: {sleep_sec}")
        time.sleep(sleep_sec)
        print(f'{cptr}: {math.floor(time.time() - time_started + 0.5)}\t current time: {time.time()}')



if __name__ == '__main__':
    start()