import pytest


@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200


@pytest.mark.others
def test_less_equal():
    num = 100
    assert num <= 100


@pytest.mark.others
def test_no_equal():
    num = 100
    assert num==num

def test_other():
    pass

def equal():
    num = 100
    assert num==100