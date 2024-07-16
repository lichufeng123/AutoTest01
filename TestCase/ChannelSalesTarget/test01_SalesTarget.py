from APIs.SalesTargetAPI import SalesTargetAPI

class TestSalesTarget:
    def setup_method(self):
        self.SalesTargetAPI = SalesTargetAPI()
    def teardown_method(self):
        pass
    def test01_getPageInfo(self):
        self.json_data = {"data": {"moduleId": "701204", "keyword": ""}, "page": 1, "pageSize": 50, "moduleId": "701204"}
        r = self.SalesTargetAPI.getPageInfo(self.json_data)
        print(r.status_code)

        # r_JsonData = r.json()["data"]
        # for id_data in r_JsonData:
        #     print(id_data["id"])
        # assert 0 == r.json()["code"]
        # assert 200 == r.status_code
        # assert 2428801492306432 == r.json()["data"][0]['id']
        #2462118772058624
