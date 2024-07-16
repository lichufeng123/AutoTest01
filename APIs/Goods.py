import requests
import config
# 重要字段：货品属性type:2单维 1多维
# 参数关联： brandId品牌 categoryId类别 patternId款型 styleId样式
# 缺陷：json数据中需要事先传入已建立好的渠道id，不然会报错,后续探索一下不加一些有独特性的条件
# 新建闭环：货品-会员体系组（+会员政策）-渠道-会员-货品库存
# 删除闭环： 货品库存-会员-渠道-会员体系组（+会员政策）-货品
class GoodsAPI:
    def __init__(self):
        self.createUrl = config.BASE_URL + '/manager/information/goods/save'
        self.updateUrl = config.BASE_URL + '/manager/information/goods/update'
        self.checkUrl = config.BASE_URL + '/manager/information/goods/check'
        self.uncheckUrl = config.BASE_URL + '/manager/information/goods/uncheck'
        self.deleteUrl = config.BASE_URL + '/manager/information/goods/delete'
        self.moduleId = "120003"
    def goodsCreate(self,json_data):
        r = requests.post(url=self.createUrl,
                             headers=config.headers,
                             json=json_data)
        return r

    def goodsUpdateValue(self,json_data):
        r = requests.put(url=self.updateUrl,
                          headers=config.headers,
                          json=json_data)
        return r

    def goodsCheck(self,json_data):
        r = requests.put(url=self.checkUrl,
                          headers=config.headers,
                          json={"data":json_data,"moduleId": self.moduleId})
        return r
    def goodsUncheck(self,json_data):
        r = requests.put(url=self.uncheckUrl,
                          headers=config.headers,
                          json={"data":json_data,"moduleId": self.moduleId})
        return r

    def goodsDelete(self,json_data):
        r = requests.post(url=self.deleteUrl,
                         headers=config.headers,
                         json={"data": json_data, "moduleId": self.moduleId})
        return r