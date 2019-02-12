import requests
from urllib3.exceptions import InsecureRequestWarning
from ansible.module_utils.basic import *

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Dashboard:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def vsc_dashboard(self):
		api_endpoint = '/api/rest/admin/dashboard'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		vsc_dashboard = r.json()
		vsc_dashboard['status_code'] = r.status_code

		return vsc_dashboard
