import pytest
import requests

from APIs.SalesTargetAPI import SalesTargetAPI

class TestSalesTarget:

    def setup_class(self):
        print("类级前置操作，只在类中前后运行一次，在类中才行")
        self.SalesTargetAPI = SalesTargetAPI()
    def teardown_class(self):
        print("类级后置操作，只在类中前后运行一次，在类中才行")
    def test01_getPageInfo(self):
        self.json_data = {"data": {"moduleId": "701204", "keyword": ""}, "page": 1, "pageSize": 50, "moduleId": "701204"}
        r = self.SalesTargetAPI.getPageInfo(self.json_data)
        print(r.status_code)
        print(r.json())
        assert 0 == r.json()["code"]
        assert 200 == r.status_code
        assert 2428801492306432 == r.json()["data"][0]['id']


if __name__ == '__main__':
    pytest.main()
