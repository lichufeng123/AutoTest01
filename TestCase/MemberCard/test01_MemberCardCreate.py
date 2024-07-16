import pytest
import requests
from APIs.MemberCard import MemberCardAPI
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


class Test_Member:
    MemberBillIdList = []
    MemberBillId = 1
    def setup_method(self):
        self.MemberCardAPI = MemberCardAPI()
    def teardown_method(self):
        pass
    # 创建会员并审核
    @pytest.mark.parametrize("data,moduleId",build_data(json_file=config.BASE_PATH+"/data/MemberCreate.json"))
    def test01_MemberSaveAndCheck(self,data,moduleId):
        json_Data = {"data": data, "moduleId": moduleId}
        # 创建
        r = self.MemberCardAPI.createMember(json_data=json_Data)
        Test_Member.MemberBillIdList.append(r.json().get('data'))
        Test_Member.MemberBillId = r.json().get('data')
        # 审核
        r1 = self.MemberCardAPI.checkMember(Test_Member.MemberBillId)
        print(r1.json())

    def test02_MemberDeleteAndUncheck(self):
        r = self.MemberCardAPI.uncheckMember(Test_Member.MemberBillId)
        print(r.json())
        r1 = self.MemberCardAPI.deleteMember(Test_Member.MemberBillIdList)
        print(r1.json())