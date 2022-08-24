import pytest

from PythonSelFramework.BaseClass1 import BaseClass1


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass1):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])

