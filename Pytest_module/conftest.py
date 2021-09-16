import pytest

@pytest.fixture #This method will be passed into the test method
def input_value():
    input = 39
    return input


