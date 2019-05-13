import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Reports:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/report/"

		if token is not None:
			self.token = token

	def get_datastores_report(self):
		api_endpoint = "datastores"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		datastore_details = r.json()
		datastore_details['status_code'] = r.status_code

		return datastore_details

	def get_virtual_machines_report(self):
		api_endpoint = "virtual-machines"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		vm_details = r.json()
		vm_details['status_code'] = r.status_code

		return vm_details
