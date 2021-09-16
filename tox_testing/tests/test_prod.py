from tox_testing.prod.prod import calc


def test_calc():
    assert calc(1,1) == 2
