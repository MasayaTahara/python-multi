import pytest
import src.simple as simple


def test_sleep1_and_return3_1():
    assert 3 == simple.sleep1_and_return3()


def test_single_thread_3():
    assert 9 == simple.single_thread(3)


def test_multi_thread_3():
    assert 9 == simple.multi_thread(3)
