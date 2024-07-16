import os
# 设置项目环境域名
# 比音勒芬



# 获取项目根路径
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)
# 比音勒芬
BASE_URL = "http://erptest.biemlf.com:21002"
Refreshtoken = 'bc4408e60bf54a19b6c40b5b5df81632'  # token
Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MjA1MjQ0NjQsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.TrFxuwF0Pxv08_lW4eXyfN76jF4j8euonilu_qXYWL0'

# 京润
# BASE_URL = "http://120.79.238.205:21001/"
# Refreshtoken = '1815d3ee3e8845bda43f9ed82f81fa6b'  # token
# Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3MjA2NzY2NTEsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.TnVJre5LEgFyVvfceuI76g7yMLSYZQK1T19hgoOKyD4'

headers={"Authorization": Authorization, "Refreshtoken": Refreshtoken}


Login_Url = 'http://erptest.biemlf.com:21002/manager/auth/accessToken'
json_data = {"userNo":"admin","password":"123123","deviceType":"web"}
# r.json().get('refreshToken')
# r.json().get('token')