import requests
import config


# 参数关联：memberTypeId levelCode levelName channelId membershipSystemId membershipSystemName
class MemberCardAPI:
    def __init__(self):
        self.createUrl = config.BASE_URL + '/manager/member/save'  # 创建会员
        self.checkUrl = config.BASE_URL + '/manager/member/check'  # 审核会员单据
        self.deleteUrl = config.BASE_URL + '/manager/member/delete' #删除会员
        self.uncheckUrl = config.BASE_URL + '/manager/member/uncheck'  # 反审核会员单据
        self.moduleId = "120009"
    def createMember(self, json_data):
        r = requests.post(url=self.createUrl,
                             headers=config.headers,
                             json=json_data)

        return r
    def checkMember(self,json_data): # 审核接口
        r = requests.put(url=self.checkUrl,
                         headers=config.headers,
                         json={"data":json_data,"moduleId": self.moduleId})
        return r

    def deleteMember(self, json_data):
        r = requests.post(url=self.deleteUrl,
                         headers=config.headers,
                         json={"data": json_data, "moduleId": self.moduleId})
        return r
    def uncheckMember(self,json_data): # 审核接口
        r = requests.put(url=self.uncheckUrl,
                         headers=config.headers,
                         json={"data":json_data,"moduleId": self.moduleId})
        return r