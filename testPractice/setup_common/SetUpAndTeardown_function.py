import pytest
import requests



def setup_function():
    print("函数级前置操作，每条用例都执行一次，不在类中才行")

def teardown_function():
    print("函数级后置操作，每条用例都执行一次，不在类中才行")

def test01_getPageInfo():
    url = 'https://retailtest.chinaerdos.com/manager/information/channelSalesTarget/page'
    Refreshtoken = 'e7b2aba915fe4adbba58e1b1f33a06dc'
    Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MTk1NTM2MjUsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.a16IEhUPR6AacjUVoCnn31Agg1z0Bjk1j-aQucR2jHk'
    json_data = {"data": {"moduleId": "701204", "keyword": ""}, "page": 1, "pageSize": 50, "moduleId": "701204"}

    r = requests.post(url=url,
                        headers={"Authorization": Authorization, "Refreshtoken": Refreshtoken},
                        json=json_data)
    print(r.status_code)
    print(r.json())
def test01_getPageInfo11():
    url = 'https://retailtest.chinaerdos.com/manager/information/channelSalesTarget/page'
    Refreshtoken = 'e7b2aba915fe4adbba58e1b1f33a06dc'
    Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MTk1NTM2MjUsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.a16IEhUPR6AacjUVoCnn31Agg1z0Bjk1j-aQucR2jHk'
    json_data = {"data": {"moduleId": "701204", "keyword": ""}, "page": 1, "pageSize": 50, "moduleId": "701204"}

    r = requests.post(url=url,
                        headers={"Authorization": Authorization, "Refreshtoken": Refreshtoken},
                        json=json_data)
    print(r.status_code)
    print(r.json())
if __name__ == '__main__':
    pytest.main()
