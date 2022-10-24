import sys
import time
import logging
import logging.handlers
import socketserver
from http.server import SimpleHTTPRequestHandler
from pathlib import Path

LOG_PATH = Path(__file__).parent / 'log'
LOG_PATH.mkdir(exist_ok=True)


def init_logger(loggername='server', level=logging.INFO):
    log = logging.getLogger(loggername)
    log.setLevel(level)

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setLevel(level)

    # fh = logging.FileHandler('log.txt', 'a', delay=True)
    # fh.setLevel(level)
    fh = logging.handlers.TimedRotatingFileHandler(
        filename= LOG_PATH / 'server.log',
        when='w6',
        backupCount=2
    )
    fh.setLevel(level)

    log.addHandler(stream)
    log.addHandler(fh)

    return log


def end_logger(loggername='server'):
    log = logging.getLogger(loggername)

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)


log = init_logger('server')


PORT = 8000


class MySimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    # def list_directory(self, path):
    #     f = super().list_directory(path)
    #     print(f.read())
    #     f.seek(0)
    #     return f

    def log_message(self, format: str, *args) -> None:
        log.info("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))


with socketserver.TCPServer(('', PORT), MySimpleHTTPRequestHandler) as httpd:
    print(f'Serving at port: {PORT}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log.warning(f"[{time.strftime('%Y/%m/%d-%H:%M:%S')}] - Receiving CTRL + C / CTRL + Z")
        end_logger()
        time.sleep(3)
        print('Exit')