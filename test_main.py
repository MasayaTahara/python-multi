import pytest
import main


def test_sleep1_and_return3_1():
    assert 3 == main.sleep1_and_return3()


def test_single_thread_3():
    assert 9 == main.single_thread(3)


def test_multi_thread_3():
    assert 9 == main.multi_thread(3)
