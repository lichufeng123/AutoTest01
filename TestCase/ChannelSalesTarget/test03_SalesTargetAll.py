import pytest
import requests
from APIs.SalesTargetAPI import SalesTargetAPI
import config
import json
def build_data(json_file):
    json_list = []
    with open(json_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            data = case_data.get("data")
            page = case_data.get("page")
            pageSize = case_data.get("pageSize")
            moduleId = case_data.get("moduleId")
            json_list.append((data,page,pageSize,moduleId))
    return json_list

# 渠道零售目标 完整的接口自动化流程

class Test_SalesTargetAll:
    def setup_method(self):
        self.SalesTargetAPI = SalesTargetAPI()
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("data,page,pageSize,moduleId",build_data(json_file=config.BASE_PATH+"/data/channeltargetData.json"))
    def test01_ChanTarget(self,data,page,pageSize,moduleId):
        self.json_Data = {"data": data,"page": page,"pageSize": pageSize,"moduleId": moduleId}
        r1 = self.SalesTargetAPI.getPageInfo(json_data=self.json_Data)
        print(r1.json())

    @pytest.mark.parametrize("data,page,pageSize,moduleId",
                             build_data(json_file=config.BASE_PATH + "/data/channeltargetData.json"))
    def test02_ChanTargetByDay(self,data,page,pageSize,moduleId):
        self.json_DayData = {"data": data, "page": page, "pageSize": pageSize, "moduleId": moduleId}
        r2 = self.SalesTargetAPI.getDayDetail(json_data=self.json_DayData)
        print(r2)

    # @pytest.mark.parametrize("data,page,pageSize,moduleId",
    #                          build_data(json_file=config.BASE_PATH + "/data/channeltargetData.json"))
    # def test03_ChanTargetByPerson(self,data,page,pageSize,moduleId):
    #     self.json_PersonData = {"data": data, "page": page, "pageSize": pageSize, "moduleId": moduleId}
    #     r3 = self.SalesTargetAPI.getPersonDetail(json_data=self.json_PersonData)

