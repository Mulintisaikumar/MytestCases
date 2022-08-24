import pytest

def test_m1():
    a = 12
    b = 7
    assert a != b,"if the test case is failed"
    assert a!=b,"Failed"

@pytest.mark.home
def test_m2():
    assert True

@pytest.mark.home
def test_m3():
    a=2
    b=5
    assert a<b,"True"
