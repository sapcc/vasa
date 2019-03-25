import requests
import os
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Commons:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def task_status(self, task_id=None):
		api_endpoint = '/api/rest/admin/task/status'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'task-id': task_id
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		task_status = r.json()
		task_status['status_code'] = r.status_code

		return task_status
