import pytest
from APIs.Channel import ChannelAPI
import config
import json
def build_data(json_file):
    json_list = []
    with open(json_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            data = case_data.get("data")
            moduleId = case_data.get("moduleId")
            json_list.append((data,moduleId))
    return json_list

# 渠道零售目标 完整的接口自动化流程

class Test_Channel:
    def setup_method(self):
        self.ChannelAPI = ChannelAPI()
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("data,moduleId",build_data(json_file=config.BASE_PATH+"/data/ChannelCreate.json"))
    def test01_ChannelCreate(self,data,moduleId):
        json_Data = {"data": data, "moduleId": moduleId}

        r = self.ChannelAPI.channelCreate(json_data=json_Data)
        print(r.json())
        print("创建货品:" + data.get('name') + "成功")
        r1 = self.ChannelAPI.channelCheck(r.json().get('data'))


