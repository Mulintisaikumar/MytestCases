import pytest

def test_m1():
    a = 3
    b = 4
    assert a+1!=b, "test faild"
    assert a!=b,"test case faild because of a is not equal to b"

def test_m2():
    name="SELENIUM"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True

@pytest.mark.login
def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100 == 100

@pytest.mark.login
def test_m6():
    assert "sai"=="sai"

@pytest.mark.login
def test_login_Gmail():
    assert "admin"=="admin"
