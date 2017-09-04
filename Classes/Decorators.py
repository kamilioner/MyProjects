# decorators
from functools import wraps


def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


def decorator_funtion(original_fuction):
    @wraps(original_fuction)
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_fuction.__name__))
        return original_fuction(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# @decorator_funtion # the same as 'dispaly = decorator_funtion(dispaly)'
# def display():
#     print('dispaly function ran')

# @decorator_class
# def dispaly_info(name, age):
#     print('dispaly info ran with arguments ({}, {})'.format(name, age))

import time


@my_logger
@my_timer  # this stack is equal to: dispaly_info = my_logger(my_timer(dispaly_info))
def dispaly_info(name, age):
    time.sleep(1)
    print('dispaly info ran with arguments ({}, {})'.format(name, age))


# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
#
# hi_func()
# bye_func()

# decorated_display = decorator_funtion(display)
# decorated_display()

dispaly_info('Hank', 30)
# display()
