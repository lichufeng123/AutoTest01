import requests
import config
# allure serve report
class SalesTargetAPI:
    def __init__(self):
        self.url = config.BASE_URL + '/manager/information/channelSalesTarget/page' # 月目标
        self.urlDayDetail = config.BASE_URL + '/manager/information/channelSalesTarget/search/salesTargetDayDetail' # 日目标
        self.urlPersonDetail = config.BASE_URL + '/manager/information/channelSalesTarget/search/salesTargetPersonDetail' # 营业员目标
        self.AddUrl = config.BASE_URL + '/manager/information/channelSalesTarget/createBatch'  # 新建渠道目标
        self.DelUrl = config.BASE_URL + '/manager/information/channelSalesTarget/delete'  # 删除渠道目标

    # 月目标Page
    def getPageInfo(self,json_data):
        return requests.post(url=self.url,
                             headers=config.headers,
                             json=json_data)

    # 日目标Page
    def getDayDetail(self,json_data):
        # 新建空列表，存储每个月目标ID
        r_getDayDetail_list = []
        # 请求月目标page接口，获取所有月目标的data
        r_JsonData = self.getPageInfo(json_data).json()["data"]
        # 遍历data，拿出id并发送日目标请求，拿出日目标的id，放入列表
        for case_data in r_JsonData:
            # 取出月目标id，放入json参数
            ParaJson = {"data": case_data.get("id"), "moduleId": "701204"}
            # 拿出日目标列表
            a= requests.post(url=self.urlDayDetail,
                             headers=config.headers,
                             json=ParaJson).json().get("data")["channelSalesTargetDayList"]
            # 遍历日目标列表，拿日目标id，放入列表
            for b in a:
                r_getDayDetail_list.append(b["id"])
        return r_getDayDetail_list

    # 营业员目标Page
    def getPersonDetail(self,json_data):
        r_getPersonDetail_list = []
        r_JsonData = self.getDayDetail(json_data)
        for case_data in r_JsonData:
            ParaJson = {"data": case_data, "moduleId": "701204"}
            c = requests.post(url=self.urlPersonDetail,
                              headers=config.headers,
                              json=ParaJson).json()
            print(c["code"])
            r_getPersonDetail_list.append(c)
        return r_getPersonDetail_list

    def addSalesTarget(self,json_data):
        r = requests.post(url=self.AddUrl,
                             headers=config.headers,
                             json=json_data).json()
        return r
    def DelSalesTargetById(self,json_data):
        return requests.post(url=self.DelUrl,
                             headers=config.headers,
                             json={"data": [json_data],"moduleId": "701204"}).json()
    def DelSalesTargetByAddList(self,json_data):
        DelChannelList = self.addSalesTarget(json_data)["data"]["succcessList"]
        r = requests.post(url=self.DelUrl,
                        headers=config.headers,
                        json={"data": DelChannelList,"moduleId": "701204"}).json()
        print("删除结束")
        return r

    def SelectByChannelYears(self,channelIdList):
        r = requests.post(url=self.url,
                          headers=config.headers,
                          json={"data": {"channelIdList":channelIdList,"keyword": "", "years":"2025-09", "moduleId": "701204" },
                                "moduleId": "701204","page": 1, "pageSize": 50}).json()
        return r