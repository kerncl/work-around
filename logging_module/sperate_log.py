import os
import logging
import logging.handlers


# Create logs directory
for roots, dirs, files in os.walk(os.getcwd()):
    if 'logs' not in dirs:
        os.mkdir('logs')
    break
logger = logging.getLogger('mylog')
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s: %(message)s')
# logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s: %(message)s')
logger.setLevel(logging.DEBUG)

# Stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Master log
# logFilePath = 'master.log'
# file_handler = logging.handlers.TimedRotatingFileHandler(filename=logFilePath, when='midnight', backupCount=30)
master_handler = logging.FileHandler(filename='logs\master.log', mode='w', delay=True)
master_handler.setFormatter(formatter)
master_handler.setLevel(logging.INFO)

# Debug log
debug_handler = logging.FileHandler(filename='logs\debug.log', mode='w', delay=True)
debug_handler.setFormatter(formatter)
debug_handler.setLevel(logging.DEBUG)

# # Info log
# info_handler = logging.FileHandler(filename='logs\Info.log', mode='w', delay=True)
# info_handler.setFormatter(formatter)
# info_handler.setLevel(logging.INFO)

# Warn log
warn_handler = logging.FileHandler(filename='logs\Warn.log', mode='w', delay=True)
warn_handler.setFormatter(formatter)
warn_handler.setLevel(logging.WARN)
warn_handler.addFilter(lambda _: _.levelno <= logging.WARNING) # Specific for Error level

# Error log
error_handler = logging.FileHandler(filename='logs\Error.fail', mode='w', delay=True)
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)
# error_handler.addFilter(lambda _: _.levelno <= logging.ERROR)   # Specific for Error level

# # Critical log
# critical_handler = logging.FileHandler(filename='logs\Critical.log', mode='w', delay=True)
# critical_handler.setFormatter(formatter)
# critical_handler.setLevel(logging.CRITICAL)


logger.addHandler(master_handler)
logger.addHandler(stream_handler)
# logger.addHandler(info_handler)
logger.addHandler(debug_handler)
logger.addHandler(warn_handler)
logger.addHandler(error_handler)
# logger.addHandler(critical_handler)


logger.info("Start")
logger.info("info logging")
logger.debug("debug logging")
# logger.warning("warning logging")
logger.error("error logging")
logger.critical("critical logging")

try:
    x = 14
    y = 0
    z = x/y
except Exception as ex:
    logger.error('Operation failed')
    logger.debug(f'Encountered {ex} when trying to perform calculation')
logger.info("Ended")

for handler in logger.handlers:
    handler.close()
    logger.removeHandler(handler)
print('Done')
