import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s starting", name)
    time.sleep(5)
    logging.info("Thread %s finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = list()
    for index in range(3):
        logging.info("Main  : create and start thread %d", index)
        x=threading.Thread(target=thread_function, args=(index,), daemon=False)  #Daemon will kill the thread if program ended without finishing the thread
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main  : before joining thread %d", index)
        thread.join()  #wait for the thread to run finish
        logging.info("Main  : thread %d done", index)

    logging.info("Main  : all done")
