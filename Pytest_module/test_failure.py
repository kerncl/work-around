'''
Test using pytest --maxfail=<num>

$pytest test_failure.py -v --maxfail=1

in this module, 3 test will be failed.
With the maxfail=1, it will stop once it reac maxfail =1
'''
import pytest
import math


def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 6


def test_sqaure_failure():
    num = 7
    assert 7 * 7 == 40


def test_equality_failure():
    assert 10 == 11

