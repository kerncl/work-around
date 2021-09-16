import logging
import math
import log2
#Create and configure logger
LOG_FORMAT = "%(levelname)s: %(name)s:%(asctime)s - %(message)s \t%(filename)s"
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=LOG_FORMAT, filemode='w') #default: WARNING
logger=logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#formatter = logging.Formatter(LOG_FORMAT)
#file_handle = logging.FileHandler('log.txt')
#file_handle.setFormatter(formatter)
#logger.addHandler(file_handle)

#Level
#NOSTSET 0
#DEBUG 10
#INFO 20
#WARNING 30
#ERROR 40
#CRITICAL 50

#Test the logger
logger.debug('This is DEBUG message from log1')
logger.info('This is INFO message from log1')
logger.warning('This is WARNING message from log1')
logger.error('This is ERROR message from log1')
logger.critical('This is CRITICAL message from log1')

def quadratic_formula (a, b, c):
    """Return the solution to equation ax^2 + bx + c =0"""
    logger.info("quadratic_formula({0}, {1}, {2})" .format(a, b, c))

    #compute the discriminat
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    #Compute the two roots
    logger.debug("#Compute the two roots")
    root1=(-b+math.sqrt(disc) / (2*a))
    root2=(-b-math.sqrt(disc) / (2*a))

    #Return the roots
    logger.debug('#Return the roots')
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)