import pytest

@pytest.mark.usefixtures("setup")
#@pytest.fixture()
class TestExample:

    def setup(self):
        print("I will be executing first ")
        yield
        print("i will be executing last")
    def test_fixtureDemo0(setup):
        print(" i will be execute steps in fixturedemo method ")

    def test_fixtureDemo1(setup):
        print(" i will be execute steps in fixturedemo method ")

    def test_fixtureDemo2(setup):
        print(" i will be execute steps in fixturedemo method ")
   
    def test_fixtureDemo3(setup):
        print(" i will be execute steps in fixturedemo method ")
