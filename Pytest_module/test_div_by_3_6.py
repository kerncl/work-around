import pytest

'''
Taking input_value method form conftest.py file with @pytest.fixture
'''
def test_divisible_by_3(input_value):
    assert input_value %3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 ==0




