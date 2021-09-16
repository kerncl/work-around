'''It will log all the executed path in the log'''

import logging
logger = logging.getLogger()
print('initialize logger :LK')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
log_pytest = logger.findCaller(stack_info=True)
logger.debug(log_pytest[0])
logger.debug(log_pytest[1])
logger.debug(log_pytest[2])
logger.debug(log_pytest[3])