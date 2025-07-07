import requests
import config
from utils.request_tool import request_with_token
# 参数关联字段:memberSystemId memberTypeId
# 会员体系组及政策 创建、删除
class MemberSystemAPI:
    PREFIX = '/manager/member/membershipSystem'
    CreateSysUrl = PREFIX+'/create' # 创建体系组
    CreatePolicyUrl = PREFIX + '/save'  # 配置会员政策
    DeleteSysUrl = PREFIX + '/delete'  # 创建体系组
    DeletePolicyUrl = PREFIX + '/delete'  # 配置会员政策


    @staticmethod
    def createSystem(customer_code,json_data):
        return request_with_token(customer_code, "POST", MemberSystemAPI.CreateSysUrl, json=json_data)

    @staticmethod
    def createPolicy(customer_code, json_data):
        return request_with_token(customer_code, "POST", MemberSystemAPI.CreatePolicyUrl, json=json_data)

    @staticmethod
    def deleteSystem(customer_code, json_data):
        return request_with_token(customer_code, "POST", MemberSystemAPI.DeleteSysUrl, json=json_data)

    @staticmethod
    def deletePolicy(customer_code, json_data):
        return request_with_token(customer_code, "POST", MemberSystemAPI.DeletePolicyUrl, json=json_data)


