import time
from functools import wraps


def processing_time(func):
    @wraps(func)
    def wrapper(*args, **keywords):
        st = time.time()
        result = func(*args, **keywords)
        print(f'time: {time.time() - st} s')
        return result
    return wrapper
