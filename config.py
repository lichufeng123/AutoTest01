import os
# 设置项目环境域名
# 比音勒芬



# 获取项目根路径
BASE_PATH = os.path.dirname(__file__)

# 演示环境
BASE_URL = "https://nebula.regentxcx.com/"
Refreshtoken = '2b20e870047a4914b9ea59822c24d6e1'  # token
Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2Vybm8iOiJhZG1pbiIsImlzcyI6InJlZ2VudHNvZnQiLCJleHAiOjg5MzA4ODAwMDAwLCJpYXQiOjE3NTA5MjE0NjQsInVzZXJpZCI6Njg3NzIzOTExMDc5NjU0M30.Hmv00QU-4aMQV5Wu95vCGAZUTZlicoGSm6_2TOsfK20'

headers={"Authorization": Authorization, "Refreshtoken": Refreshtoken}


# Login_Url = 'http://erptest.biemlf.com:21002/manager/auth/accessToken'
# json_data = {"userNo":"admin","password":"123123","deviceType":"web"}
# r.json().get('refreshToken')
# r.json().get('token')