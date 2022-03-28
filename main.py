from time import sleep
from concurrent import futures
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


def sleep1_and_return3() -> int:
    sleep(1)
    return 3


@processing_time
def single_thread(times: int) -> int:
    sum = 0
    for _ in range(times):
        sum += sleep1_and_return3()
    return sum


@processing_time
def multi_thread(times: int) -> int:
    sum = 0
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        for _ in range(times):
            future = executor.submit(sleep1_and_return3)
            result = future.result()
            sum += result
        _ = futures.as_completed(fs=sum)
    return sum
