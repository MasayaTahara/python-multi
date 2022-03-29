from time import sleep
from concurrent.futures import ThreadPoolExecutor
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
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for _ in range(times):
            futures.append(executor.submit(sleep1_and_return3))
    return sum([f.result() for f in futures])


class Validator:
    def __init__(self):
        self.sum = 0

    def _sleep1_and_add3(self):
        sleep(1)
        self.sum += 3
        return

    @processing_time
    def _single_thread(self, times: int) -> int:
        for _ in range(times):
            self._sleep1_and_add3()
        return self.sum

    @processing_time
    def _multi_thread(self, times: int) -> int:
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            for _ in range(times):
                futures.append(executor.submit(self._sleep1_and_add3))
        return self.sum
