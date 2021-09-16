import socket
PORT = 1234

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('localhost', PORT))
mysocket.makefile('r')


# ### Initialize Logging ###
# log = logging.getLogger('mylog')
# log.setLevel(logging.INFO)
# # socket stream
# socket_stream_fh = logging.StreamHandler(file)
# socket_stream_fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] - %(filename)s: %(message)s"))
# socket_stream_fh.setLevel(logging.INFO)
# log.addHandler(socket_stream_fh)
# # stream
# stream_fh = logging.StreamHandler(sys.stdout)
# stream_fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] - %(filename)s: %(message)s"))
# stream_fh.setLevel(logging.INFO)
# log.addHandler(stream_fh)

import socketserver
socketserver.ThreadingTCPServer
socketserver.StreamRequestHandler