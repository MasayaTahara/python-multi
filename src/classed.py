from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading
from src.util import processing_time


class Validator:
    lock = threading.Lock()

    def __init__(self):
        self.sum = 0

    def _sleep1_and_add_without_lock(self):
        sleep(1)
        for _ in range(1_000_000):
            self.sum += 1
        return

    def _sleep1_and_add_with_lock(self):
        sleep(1)
        for _ in range(1_000_000):
            with self.lock:
                self.sum += 1
        return

    @processing_time
    def _single_thread(self, times: int) -> int:
        for _ in range(times):
            self._sleep1_and_add_without_lock()
        return self.sum

    @processing_time
    def _multi_thread_without_lock(self, times: int) -> int:
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            for _ in range(times):
                futures.append(executor.submit(
                    self._sleep1_and_add_without_lock))
        return self.sum

    @processing_time
    def _multi_thread_with_lock(self, times: int) -> int:
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            for _ in range(times):
                futures.append(executor.submit(
                    self._sleep1_and_add_with_lock))
        return self.sum
