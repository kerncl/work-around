from concurrent.futures import ThreadPoolExecutor
import logging
import time


def thread_function(name):
    logging.info("Thread %s starting", name)
    time.sleep(5)
    logging.info("Thread %s finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    with ThreadPoolExecutor(max_workers=3) as executor: #with : context manager --> auto assign join() statment for the threading
        executor.map(thread_function, range(3))
