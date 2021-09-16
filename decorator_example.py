# Decorators using class:
def decorater_function(orig_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper excuted this before {} function'.format(orig_function.__name__))
        return orig_function(*args, **kwargs)  # execution so need the args

    return wrapper_function  # return function without execution


class decorator_class(object):
    def __init__(self, orig_function):
        self.orig_function = orig_function

    def __call__(self, *args, **kwargs):  # wrapper function
        print('call method executed this before {} function'.format(self.orig_function.__name__))
        return self.orig_function(*args, **kwargs)


@decorator_class  # display = decorator_class(display)
def display_class():
    print('display function ran')


@decorator_class
def display_info_class(name, age):
    print('display_info ran with args {0} {1}'.format(name, age))


print('Showing Class decorator')
display_class()
display_info_class('linn kern', 25)

# Decorator using function:
from functools import wraps


def my_logger(orig_function):
    import logging
    log_format = '%(levelname)s: %(name)s: %(asctime)s- %(message)s'
    logging.basicConfig(filename='{}.log'.format(orig_function.__name__),
                        level=logging.DEBUG,
                        filemode='w',
                        format=log_format)

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs:{}'.format(args, kwargs))
        return orig_function(*args, **kwargs)

    return wrapper


def my_timer(orig_function):
    import time
    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_function.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info_func(name, age):
    time.sleep(1)
    print('Display_info ran with arguments ({0} {1})'.format(name, age))


print('Display function decorator')
display_info_func('ZQ', 25)
