import requests
import config

# 参数关联字段:memberSystemId memberTypeId
# 会员体系组及政策 创建、删除
class MemberSystemAPI:
    def __init__(self):
        self.CreateSysUrl = config.BASE_URL + '/manager/member/membershipSystem/create'  # 创建体系组
        self.CreatePolicyUrl = config.BASE_URL + '/manager/member/policy/save'  # 配置会员政策
        self.DeleteSysUrl = config.BASE_URL + '/manager/member/membershipSystem/delete'  # 创建体系组
        self.DeletePolicyUrl = config.BASE_URL + '/manager/member/policy/delete'  # 配置会员政策
        self.SystemModuleId = "121047"
        self.PolicyModuleId = "120010"
    def createSystem(self, json_data):
        r = requests.post(url=self.CreateSysUrl,
                             headers=config.headers,
                             json=json_data)
        return r
    def createPolicy(self, json_data):
        r = requests.post(url=self.CreatePolicyUrl,
                             headers=config.headers,
                             json=json_data)
        return r
    def deleteSystem(self, json_data):
        r = requests.post(url=self.DeleteSysUrl,
                             headers=config.headers,
                             json={"data":json_data,"moduleId":self.SystemModuleId})
        return r
    def deletePolicy(self, json_data):
        r = requests.post(url=self.DeletePolicyUrl,
                             headers=config.headers,
                             json={"data":json_data,"moduleId":self.PolicyModuleId})
        return r


