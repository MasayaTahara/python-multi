from time import sleep
from concurrent.futures import ThreadPoolExecutor
from src.util import processing_time


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
