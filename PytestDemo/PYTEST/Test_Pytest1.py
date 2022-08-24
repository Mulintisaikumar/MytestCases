import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def testMethod1():
    print("This is test methos 1")

def testMethod2():
    print("This is test method 2")
