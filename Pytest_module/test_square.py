import math
import pytest
'''
Any method name that consist of test*
To run :
--> in terminal
    --> pytest -v
'''
@pytest.mark.square
def test_sqrt():    #work
    num = 25
    assert math.sqrt(num)==5

@pytest.mark.square
def testsquare():   #work
    num = 7
    assert 7*7 == 40


def tesquality():     #notwork
    assert 10 == 11


@pytest.mark.others
def test_equality():
    assert 10 == 11