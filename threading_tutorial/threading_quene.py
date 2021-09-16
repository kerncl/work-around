import random
import logging
import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor

SENTINEL = object()


def producer(pipeline):
    """Pretend we're getting a message from the network"""
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    #Send a sentinel message to tell consumer we 're done
    logging.info("Producer recevied EXIT event. Exiting")


def consumer(pipeline):
    """Pretend we're saving a number in the database"""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info("Consumer storing message: %s (queue size=%s)", message, pipeline.qsize())
    logging.info("Consumer recevied EXIT event. Existing")


class Pipeline(queue.Queue):
    ''' Class to allow a single element pipeline between producer and consumer'''

    def __init__(self):
        super().__init__(maxsize=10)


    def get_message(self, name):    #consumer
        logging.debug("%s: about to get from queue", name)
        value = self.get()
        logging.debug("%s got %d from queue", name, value)

    def set_message(self, value, name):   #producer
        logging.debug("%s: about to acquire setlock", name)
        self.put(value)
        logging.debug("%s: added %d to queue", name, value)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    event = threading.Event()
    with ThreadPoolExecutor (max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
        time.sleep(0.1)
        logging.info("Main about to set event")
        event.set()