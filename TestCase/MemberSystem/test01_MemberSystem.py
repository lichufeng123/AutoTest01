import logging

import pytest
from APIs.MemberSystem import MemberSystemAPI
from utils.data_utils import build_data
import config
import json




class Test_MemberSystem:
    # 存储创建会员体系组和政策返回的id
    memberSystemId = ''
    memberSystemList = []
    memberPolicyList = []
    def setup_method(self):
        pass
    def teardown_method(self):
        pass
    # 参数化从文件取值
    @pytest.mark.parametrize("data,moduleId",build_data(json_file=config.BASE_PATH+"/data/MemberSystem.json", keys=("data","moduleId")))
    def test01_MemberSystemCreate(self,data,moduleId):
        # 将文件中拿的值组合成json数据，用来入参
        json_Data = {"data": data, "moduleId": moduleId}
        # 创建会员体系组
        r = MemberSystemAPI.createSystem("customer_a",json_data= json_Data)
        # 存储创建会员体系组返回的id，存为数值和list
        # Test_MemberSystem.memberSystemId = r.json().get('data')
        # Test_MemberSystem.memberSystemList.append(r.json().get('data'))

    # 参数化从文件取值
    @pytest.mark.parametrize("data,moduleId", build_data(json_file=config.BASE_PATH + "/data/MemberPolicy.json"))
    def test02_MemberPolicyCreate(self, data, moduleId):
        # 替换文件拿的data值中的memberSystemId字段
        data.update({
            "memberSystemId":Test_MemberSystem.memberSystemId
                     })
        # 组合成json数据
        json_Data = {"data": data, "moduleId": moduleId}
        # 创建会员政策
        r = self.MemberSystemAPI.createPolicy(json_data=json_Data)
        # 存储创建会员政策返回的id，存为list
        Test_MemberSystem.memberPolicyList.append(r.json().get('data'))

    # 删除会员政策
    def test03_MemberPolicyDelete(self):
        r = self.MemberSystemAPI.deletePolicy(Test_MemberSystem.memberPolicyList)
        print(r.json()['code'])

    # 删除会员体系组
    def test04_MemberSystemDelete(self):
        r = self.MemberSystemAPI.deleteSystem(Test_MemberSystem.memberSystemList)
        print(r.json()['code'])

