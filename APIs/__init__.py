import requests

# url = 'https://retailtest.chinaerdos.com/manager/information/channelSalesTarget/page'
# Refreshtoken = 'e7b2aba915fe4adbba58e1b1f33a06dc'
# Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MTk1NTM2MjUsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.a16IEhUPR6AacjUVoCnn31Agg1z0Bjk1j-aQucR2jHk'
# json_data = {"data":{"moduleId":"701204","keyword":""},"page":1,"pageSize":50,"moduleId":"701204"}
url = 'https://www.imooc.com/activity/baseinfo'
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
r = requests.get(url=url,
                  headers={"User-Agent": User_Agent})
print(r.status_code)
print(r.json())


