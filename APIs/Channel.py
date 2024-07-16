import requests
import config

class ChannelAPI:
    def __init__(self):
        self.createUrl = config.BASE_URL + '/manager/information/channel/create'
        self.updateUrl = config.BASE_URL + '/manager/information/channel/update'
        self.checkUrl = config.BASE_URL + '/manager/information/channel/check'
        self.moduleId = "120001"

    def channelCreate(self,json_data):
        r = requests.post(url=self.createUrl,
                             headers=config.headers,
                             json=json_data)
        return r

    def channelUpdateValue(self,json_data):
        r = requests.put(url=self.updateUrl,
                          headers=config.headers,
                          json=json_data)
        return r

    def channelCheck(self,json_data):
        r = requests.put(url=self.checkUrl,
                          headers=config.headers,
                          json={"data":json_data,"moduleId": self.moduleId})
        return r