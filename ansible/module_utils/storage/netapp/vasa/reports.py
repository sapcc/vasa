import requests
from urllib3.exceptions import InsecureRequestWarning
from ansible.module_utils.basic import *

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Reports:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def datastores(self):
		api_endpoint = '/api/rest/admin/report/datastores'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		datastore_details = r.json()
		datastore_details['status_code'] = r.status_code

		return datastore_details

	def virtual_machines(self):
		api_endpoint = '/api/rest/admin/report/virtual-machines'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		vm_details = r.json()
		vm_details['status_code'] = r.status_code

		return vm_details
