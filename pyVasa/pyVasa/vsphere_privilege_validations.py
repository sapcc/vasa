import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class VspherePrivilegdeValidations:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port + "/" + self.api
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def show_privilidges(self, privilegeId=None):
		api_endpoint = '/api/rest/vcenter/privileges?privilegeId=' + privilegeId
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		priv_details = r.json()
		priv_details['status_code'] = r.status_code

		return priv_details
