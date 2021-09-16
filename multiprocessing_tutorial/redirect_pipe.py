import threading
import os
import sys
import rpyc
import datetime
import time
from rpyc.utils.server import ThreadedServer
import inspect

PORT = 19961


class MyService(rpyc.Service):

    def on_connect(self, conn):
        print(f'\n Connect on {datetime.time()}')
        time.sleep(1)

    def exposed_execute(self, data):
        print(data)

    def on_disconnect(self, conn):
        print(f"Disconnected on {datetime.time()}")

    def exposed_read_file(self):
        count = 0
        with open('temp.txt', 'r') as f:
            yield f.readline(1024)
            print(count)
            count  +=1


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # server
        print('Start Service')
        t = ThreadedServer(MyService(), port=PORT)
        t.start()
    else:
        conn = rpyc.connect('localhost', port=PORT)
        conn.root.execute('hello')
        gen = conn.root.read_file()
        for line in gen:
            print(line)
