import pytest
import requests


json_data = [
    ( 1, 50, '701204',{'moduleId': '701204', 'keyword': ''}),
    ( 1, 25, '701204',{'moduleId': '701204', 'keyword': ''})
             ]
@pytest.mark.parametrize("page,pageSize,moduleId,data",json_data)
def test01_getPageInfo(page,pageSize,moduleId,data):
    url = 'https://retailtest.chinaerdos.com/manager/information/channelSalesTarget/page'
    Refreshtoken = 'e7b2aba915fe4adbba58e1b1f33a06dc'
    Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MTk1NTM2MjUsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.a16IEhUPR6AacjUVoCnn31Agg1z0Bjk1j-aQucR2jHk'
    json_data = {"page": page, "pageSize": pageSize, "moduleId": moduleId, "data": data}

    r = requests.post(url=url,
                        headers={"Authorization": Authorization, "Refreshtoken": Refreshtoken},
                        json=json_data)
    print(json_data)
    assert 0 == r.json()["code"]
    assert 200 == r.status_code