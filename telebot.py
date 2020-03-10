import requests


class Bot:

    def __init__(self, token, proxy):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.r = requests.Session()
        self.r.proxies = proxy

    def get_updates(self, new_offset):
        """

        :param new_offset:
        :return:
        """
        method = 'getUpdates'
        params = {'offset': new_offset}
        resp = self.r.get(self.api_url + method, data=params)
        return resp.json()['result']
