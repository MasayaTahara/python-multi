import pytest
from src.classed import Validator


def test_single_thread_in_class():
    validator = Validator()
    assert 3_000_000 == validator._single_thread(3)


def test_multi_thread_without_lock_in_class():
    validator = Validator()
    assert 3_000_000 > validator._multi_thread_without_lock(3)


def test_multi_thread_with_lock_in_class():
    validator = Validator()
    assert 3_000_000 == validator._multi_thread_with_lock(3)
