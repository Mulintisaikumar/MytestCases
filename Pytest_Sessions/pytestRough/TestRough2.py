import pytest


def test_total_divisble_by_100(input_total):
    assert input_total % 100 == 0

def test_total_divisble_by_15(input_total):
    assert input_total % 15 == 0
