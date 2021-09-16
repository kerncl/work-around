import sys
import threading
import signal
import time

import rpyc
import logging
import logging.handlers

PORT = 19961

format = '%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s'
format_fh = logging.Formatter(format)
log = logging.getLogger('mylog')
log.setLevel(logging.INFO)

# Stream
stream_fh = logging.StreamHandler(sys.stdout)
stream_fh.setFormatter(format_fh)
log.addHandler(stream_fh)

# File
file_fh = logging.FileHandler('server.log', mode='w', delay=True)
file_fh.setFormatter(format_fh)
log.addHandler(file_fh)

# Socket
socket_fh = logging.handlers.SocketHandler('localhost',
                                           logging.handlers.DEFAULT_TCP_LOGGING_PORT)
socket_fh.setFormatter(format_fh)
log.addHandler(socket_fh)

log.info('Testing 123')


class myService(rpyc.Service):

    def exposed_execute(self, value):
        log.info(f'Calling from server: received value {value}')
        return f'Server Modify: {value}'

    @staticmethod
    def exposed_kill():
        log.info(f'Going to kill service')
        t = threading.Timer(1.0, server.close)
        t.daemon = True
        t.start()
        # time.sleep(1)
        return 0


def handler(signum, frame):
    log.info(f'Received CTRL+C')
    myService.exposed_kill()
    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
    log.info('DONE')
    exit(0)


if __name__ == '__main__':
    print('Going to Start Service')
    server = rpyc.utils.server.ThreadedServer(myService(), port=PORT)
    signal.signal(signal.SIGINT, handler)
    print('Service start soon')
    server.start()