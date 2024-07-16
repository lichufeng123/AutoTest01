import requests
import config
# 货品库存调整单 此处用作渠道、货品写死的情况使用
# 缺陷：目前json数据中的渠道和货品入参写死
class GoodsInventoryAPI:
    def __init__(self):
        self.createUrl = config.BASE_URL + '/manager/information/stockAdjustBill/create'
        self.updateUrl = config.BASE_URL + '/manager/information/stockAdjustBill/update'
        self.checkUrl = config.BASE_URL + '/manager/information/stockAdjustBill/check'
        self.uncheckUrl = config.BASE_URL + '/manager/information/stockAdjustBill/uncheck'
        self.deleteUrl = config.BASE_URL + '/manager/information/stockAdjustBill/delete'
        self.moduleId = "809999"

    def goodsInventoryCreate(self, json_data):
        r = requests.post(url=self.createUrl,
                          headers=config.headers,
                          json=json_data)
        return r

    def goodsInventoryDelete(self, json_data):
        r = requests.post(url=self.deleteUrl,
                          headers=config.headers,
                          json={"data": json_data, "moduleId": self.moduleId})
        return r

    def goodsInventoryUpdateValue(self, json_data):
        r = requests.put(url=self.updateUrl,
                         headers=config.headers,
                         json=json_data)
        return r

    def goodsInventoryCheck(self, json_data):
        r = requests.put(url=self.checkUrl,
                         headers=config.headers,
                         json={"data": json_data, "moduleId": self.moduleId})
        return r

    def goodsInventoryUnCheck(self, json_data):
        r = requests.put(url=self.uncheckUrl,
                         headers=config.headers,
                         json={"data": json_data, "moduleId": self.moduleId})
        return r