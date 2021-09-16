import random
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

SENTINEL = object()
p = 0
c = 0


def producer(pipeline):
    """Pretend we're getting a message from the network"""
    for index in range(10):
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    #Send a sentinel message to tell consumer we 're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """Pretend we're saving a number in the database"""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


class Pipeline:
    ''' Class to allow a single element pipeline between producer and consumer'''

    def __init__(self):
        self.p = 0
        self.c = 0
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
        logging.debug("Consumer lock: {con}, Producer lock: {pro}".format(con=self.c, pro=self.p))
        self.c +=1
        logging.debug("Consumer lock: {con}, Producer lock: {pro}" .format(con=self.c, pro=self.p))

    def get_message(self, name):    #consumer
        logging.debug("%s\t: about to acquire getlock", name)
        self.consumer_lock.acquire()
        self.c +=1
        logging.debug("Consumer lock: {con}, Producer lock: {pro}".format(con=self.c, pro=self.p))
        logging.debug("%s: have getlock", name)
        message = self.message
        logging.debug("%s\t: about to release setlock", name)
        self.producer_lock.release()
        self.p -=1
        logging.debug("Consumer lock: {con}, Producer lock: {pro}".format(con=self.c, pro=self.p))
        logging.debug("%s\t: setlock released", name)
        return message

    def set_message(self, message, name):   #producer
        logging.debug("%s: about to acquire setlock", name)
        self.producer_lock.acquire()
        self.p +=1
        logging.debug("Consumer lock: {con}, Producer lock: {pro}".format(con=self.c, pro=self.p))
        logging.debug("%s: have setlock", name)
        self.message = message
        logging.debug("%s: about to release getlock", name)
        self.consumer_lock.release()
        self.c -=1
        logging.debug("Consumer lock: {con}, Producer lock: {pro}".format(con=self.c, pro=self.p))
        logging.debug("%s: getlock released", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.NOTSET)
    pipeline = Pipeline()
    with ThreadPoolExecutor (max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
