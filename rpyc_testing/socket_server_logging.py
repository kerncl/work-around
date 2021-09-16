import os
import pickle
import logging
import logging.handlers
import socketserver
import struct
import threading
import signal
import sys


class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    """Handler for a streaming logging request.

    This basically logs the record using whatever logging policy is
    configured locally.
    """

    def handle(self):
        """
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format. Logs the record
        according to whatever policy is configured locally.
        """
        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            obj = pickle.loads(chunk)
            record = logging.makeLogRecord(obj)
            self.handleLogRecord(record)

    def handleLogRecord(self, record):
        # if a name is specified, we use the named logger rather than the one
        # implied by the record.
        if self.server.logname is not None:
            name = self.server.logname
        else:
            name = record.name
        logger = logging.getLogger(name)
        # N.B. EVERY record gets logged. This is because Logger.handle
        # is normally called AFTER logger-level filtering. If you want
        # to do filtering, do it at the client end to save wasting
        # cycles and network bandwidth!
        logger.handle(record)


class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
    """
    Simple TCP socket-based logging receiver suitable for testing.
    """

    allow_reuse_address = True
    loop_flag = threading.Event()
    loop_flag.set()

    def __init__(self, host='localhost',
                 port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
                 handler=LogRecordStreamHandler):
        socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.timeout = 1
        self.logname = None

    @classmethod
    def serve_until_stopped(cls):
        self = cls()
        import select
        while type(self).loop_flag.is_set():
            rd, wr, ex = select.select([self.socket.fileno()],
                                       [], [],
                                       self.timeout)
            if rd:
                self.handle_request()


def main():
    logging.basicConfig(
        format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')



    print('About to start TCP server...')
    print(f'PID: {os.getpid()}')
    # t = threading.Thread(target=LogRecordSocketReceiver.serve_until_stopped)
    # signal.signal(signal.SIGTERM, handler)
    # t.start()
    # t.join()
    print('START !!!')
    LogRecordSocketReceiver.serve_until_stopped()


if __name__ == '__main__':
    def handler(signum, frame):
        print('Received: CTRL+C')
        print(f'signum: {signum}, frame:{dir(frame)}')
        LogRecordSocketReceiver.loop_flag.clear()
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    main()