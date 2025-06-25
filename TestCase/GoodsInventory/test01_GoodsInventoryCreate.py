import pytest
import requests
from APIs.GoodsInventory import GoodsInventoryAPI
from utils.assert_utils import log_and_assert_response
from utils.data_utils import build_data
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


class Test_GoodsInventory:
    GoodsInventoryBillIdList = []
    GoodsInventoryBillId = 1
    def setup_method(self):
        self.GoodsInventoryAPI = GoodsInventoryAPI()

    def teardown_method(self):
        pass
    # 新用法
    # @pytest.mark.parametrize("page,pageSize,moduleId", build_data("xxx.json", keys=("page", "pageSize", "moduleId")))
    @pytest.mark.parametrize("data,moduleId",build_data(json_file=config.BASE_PATH+"/data/GoodsInventoryCreate.json"))
    def test01_Create(self,data,moduleId):

        json_Data = {"data": data,"flag": 0, "moduleId": moduleId}
        # 创建库存单
        with allure.step("创建库存单"):
            r = self.GoodsInventoryAPI.goodsInventoryCreate(json_data=json_Data)
            log_and_assert_response(r, expect_code=200, description="库存单创建接口")
        #存储库存单单据编号
        Test_GoodsInventory.GoodsInventoryBillId = r.json().get('data')
        Test_GoodsInventory.GoodsInventoryBillIdList.append(r.json().get('data'))
        # 审核库存
        r1 = self.GoodsInventoryAPI.goodsInventoryCheck(r.json().get('data'))
        # 人工断言 后续换成assert

    # 删除库存
    def test02_delete(self):

        r = self.GoodsInventoryAPI.goodsInventoryUnCheck(json_data=Test_GoodsInventory.GoodsInventoryBillId)
        r1 = self.GoodsInventoryAPI.goodsInventoryDelete(json_data=Test_GoodsInventory.GoodsInventoryBillIdList)

        if r.status_code == 200:
            print("单据反审核成功")
        if r1.status_code == 200:
            print("单据删除成功")


