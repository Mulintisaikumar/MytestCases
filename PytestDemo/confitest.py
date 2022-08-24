import params as params
import pytest


@pytest.fixture()
def setup(request):
    print("I will be executing first ")
    yield
    print("I will be executed last ")


@pytest.fixture(scope = "class")
def dataLoad():
    print(" user profile data is being created")
    return ["sai","Kumar","saiKumar.com"]

@pytest.fixture(params=[("chrome", "sai","Kumar"),("Firefox", "Sai"),("IE","Kumar")])
def crossBrowser(request):
    return request.param
print('@pytest.fixture(params=[("chrome", "sai","Kumar"),("Firefox", "Sai"),("IE","Kumar")])')
print(params)