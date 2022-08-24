#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
# Any code should be wrapped in method only
#frame work is an organised way of maintaining automation files.

import pytest
@pytest.fixture()
def test_firstProgram(setup):
    print('Hello')


@pytest.mark.xfail
def test_SecondGreetCreaditCard():
    print('Good Morning')

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
