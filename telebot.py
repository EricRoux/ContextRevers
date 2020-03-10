import requests


class Bot:

    def __init__(self, token, proxy):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.r = requests.Session()
        self.r.proxies = proxy

    def get_updates(self, new_offset):
        """
        Use this method to receive incoming updates. It returns a json list of Update objects.
        :param new_offset:  Identifier of the first update to be returned.
        :return:            json result
        """
        method = 'getUpdates'
        params = {'offset': new_offset}
        resp = self.r.get(self.api_url + method, data=params)
        return resp.json()['result']
