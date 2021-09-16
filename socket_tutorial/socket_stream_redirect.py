import os
import socket
import logging
import sys
import multiprocessing
import threading

PORT = 1234
HOST = 'localhost'


def initListenerSocket(port=PORT):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((HOST, port))
    mysocket.listen(5)
    conn, addr = mysocket.accept()
    return conn


def redirectOut(port=PORT, host=HOST):
    """
    connect caller's std.out stream to a socket for GUI to listen start caller after
    listener started, else connect fails before accept
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    file = mysocket.makefile('w')
    sys.stdout = file
    return mysocket


def redirectIn(port=PORT, host=HOST):
    """
    connect caller's standard input stream to a socket for GUI to provide
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    file = mysocket.makefile('r')
    sys.stdin = file
    return mysocket


def redirectBothAsClient(port=PORT, host=HOST):
    """
    connect caller's standard input stream to a socket for GUI to provide
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    ofile = mysocket.makefile('w')
    ifile = mysocket.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return mysocket


def redirectBothAsServer(port=PORT, host=HOST):
    """
    connect caller's standard input and output stream to same socket in this mode, caller
    is server to a client: receives msg, send reply
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((host, port))
    mysocket.listen(5)
    conn, addr = mysocket.accept()
    ofile = conn.makefile('w')
    ifile = conn.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return conn


def server1():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print(f'Server {mypid} got [{data}]')


def client1():
    mypid = os.getpid()
    redirectOut()
    for i in range(3):
        print(f'client {mypid} : {i}')
        sys.stdout.flush()


def server2():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile()
    for i in range(3):
        conn.send((f'server {mypid}: {i}\n').encode())


def client2():
    mypid = os.getpid()
    redirectIn()
    for i in range(3):
        data = input()
        print(f'client {mypid} got {data}')


def server3():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        conn.send((f'Server {mypid} got [{data}]').encode())


def client3():
    mypid = os.getpid()
    redirectBothAsClient()
    for i in range(3):
        print(f'Client {mypid}: {i}')
        data = input()
        sys.stderr.write(f'client {mypid} got [{data}]\n')


if __name__ == '__main__':
    multiprocessing.Process(target=server3, daemon=True).start()
    client3()