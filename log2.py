import logging
LOG_FORMAT2 = "%(levelname)s: %(name)s:%(asctime)s - %(message)s \t%(filename)s"
logging.basicConfig(filename='log2.txt', format=LOG_FORMAT2, filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#formatter = logging.Formatter(LOG_FORMAT2)
#file_handle = logging.FileHandler('log2.txt')
#file_handle.setFormatter(formatter)
#logger.addHandler(file_handle)

logger.debug('This is DEBUG message from log2')
logger.info('This is INFO message from log2')
logger.warning('This is WARNING message from log2')
logger.error('This is ERROR message from log2')
logger.critical('This is CRITICAL message from log2')
