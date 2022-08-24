#Any pytest file should start with test_
#pytest method names should start with test
# Any code should be wrapped in method only
#method name should have sense
# -k stands for method names execution,  -s logs in out put   -v stands for more info metadata
#you can specific file with py.test (filename>
# you can mark(tag) tests @pytest.py.smoke and then run with -m
#you can skip test with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down method for test cases- confit file to generalize fixt
#fixture and make it available to all test cases
#data and parameterization can be done with return statement in tuple format
#when you define fixture scope to class omly,it will run once before class is initiated and at the end

import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg ="Hello" #operations
    assert msg == "Hi", "Test field because strings do not match"

#def test_secondProgram():
def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6  #addition do not match

@pytest.fixture()
def setup():
    print("I will be executing first ")

def test_fixtureDemo():
    print(" i will execute steps in fixtureDemo method")
