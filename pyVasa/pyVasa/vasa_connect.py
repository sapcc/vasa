import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class VasaConnection:
    token = None

    def __init__(self, url=None, port=None, vcenter_user=None, vcenter_password=None, api_version='1.0'):
        self.api = api_version
        self.port = port + "/" + self.api
        self.url = "https://" + url
        self.vcenter_user = vcenter_user
        self.vcenter_password = vcenter_password

    def new_token(self):
        api_endpoint = '/api/rest/user/login'
        url_action = self.url + ":" + self.port + api_endpoint
        headers = {'Accept': 'application/json'}
        payload = {
            'vcenterPassword': self.vcenter_password,
            'vcenterUserName': self.vcenter_user
        }

        r = requests.post(url=url_action, headers=headers, json=payload)

        self.token = r.json()['vmwareApiSessionId']

        return self.token

    def logout(self):
        api_endpoint = '/api/rest/user/logout'
        url_action = self.url + ":" + self.port + api_endpoint
        headers = {
            'Accept': 'application/json',
            'vmware-api-session-id': self.token
        }

        r = requests.post(url=url_action, headers=headers, verify=False)

        out = r.json()
        out['status_code'] = r.status_code

        return out
