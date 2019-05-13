import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class UserAuthentication:
    token = None

    def __init__(self, url=None, port=None, vcenter_user=None, vcenter_password=None, api_version='1.0'):
        self.api = api_version
        self.port = port
        self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/user/"
        self.vcenter_user = vcenter_user
        self.vcenter_password = vcenter_password

    def login(self):
        api_endpoint = "login"
        url_action = self.url + api_endpoint

        headers = {'Accept': 'application/json'}
        payload = {
            'vcenterPassword': self.vcenter_password,
            'vcenterUserName': self.vcenter_user
        }

        r = requests.post(url=url_action, headers=headers, json=payload)

        token = dict()

        if r.json()['responseMessage']:
            token['responseMessage'] = r.json()['responseMessage']
            token['vmwareApiSessionId'] = r.json()['vmwareApiSessionId']

        token['status_code'] = r.status_code

        return token

    def logout(self, token=None):
        api_endpoint = "logout"
        url_action = self.url + api_endpoint
        headers = {
            'Accept': 'application/json',
            'vmware-api-session-id': token
        }

        r = requests.post(url=url_action, headers=headers, verify=False)

        out = dict()

        if r.json()['responseMessage']:
            out['responseMessage'] = r.json()['responseMessage']

        out['status_code'] = r.status_code

        return out
