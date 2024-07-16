import pytest
import requests
from APIs.SalesTargetAPI  import SalesTargetAPI
import config
import json

def build_data(json_file):
    json_list = []
    with open(json_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            data = case_data.get("data")
            moduleId = case_data.get("moduleId")
            json_list.append((data, moduleId))
            # 传两个参数的话就要括号包起来，parametrize自动把两个元祖分给两个参数，实际上参数还是list
    return json_list

def build_data1(json_file):
    json_list = []
    with open(json_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            data = case_data.get("data")
            json_list.append(data)
            # 传一个参数的话就不要括号包起来，不然实际上参数是元祖类型
    return json_list
# 渠道零售目标 完整的接口自动化流程

class Test_SalesTargetAll:
    def setup_method(self):
        self.SalesTargetAPI = SalesTargetAPI()
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("data, moduleId",build_data(json_file=config.BASE_PATH+"/data/AddChannelTargetData.json"))
    def test01_AddChanTarget(self,data, moduleId):
        json_Data = {"data": data, "moduleId": moduleId}
        r1 = self.SalesTargetAPI.addSalesTarget(json_data=json_Data)
        print(r1)

    @pytest.mark.parametrize("data, moduleId",
                             build_data(json_file=config.BASE_PATH + "/data/AddChannelTargetData.json"))
    def test02_SelectByChannelYears(self,data, moduleId):
        channelIdList = []
        for test_data in data:
            channelId = test_data["channelId"]
            channelIdList.append(channelId)
        r1 = self.SalesTargetAPI.SelectByChannelYears(channelIdList=channelIdList)
        print(r1)


    @pytest.mark.parametrize("data, moduleId",
                             build_data(json_file=config.BASE_PATH + "/data/AddChannelTargetData.json"))
    def test03_DelChanTarget(self,data, moduleId):
        self.json_Data = {"data": data, "moduleId": moduleId}
        r = self.SalesTargetAPI.DelSalesTargetByAddList(json_data=self.json_Data)
        print(r)




