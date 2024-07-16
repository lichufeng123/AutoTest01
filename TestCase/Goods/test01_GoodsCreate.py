import pytest
import requests
from APIs.Goods import GoodsAPI
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

class Test_Goods:
    GoodsBillIdList = []
    GoodsBillId = 1
    def setup_method(self):
        self.GoodsAPI = GoodsAPI()
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("data,moduleId",build_data(json_file=config.BASE_PATH+"/data/GoodsCreate.json"))
    def test01_GoodsCreate(self,data,moduleId):
        json_Data = {"data": data, "moduleId": moduleId}
        r = self.GoodsAPI.goodsCreate(json_data=json_Data)
        # 存储货品单号id
        Test_Goods.GoodsBillIdList.append(r.json().get('data'))
        Test_Goods.GoodsBillId = r.json().get('data')
        #审核货品
        r1 = self.GoodsAPI.goodsCheck(r.json().get('data'))

    def test02_GoodsDelete(self):
        r = self.GoodsAPI.goodsUncheck(json_data=Test_Goods.GoodsBillId)
        r1 = self.GoodsAPI.goodsDelete(json_data=Test_Goods.GoodsBillIdList)


