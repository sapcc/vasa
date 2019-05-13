import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Task:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/task/"

		if token is not None:
			self.token = token

	def get_task_status(self, task_id=None):
		api_endpoint = "status"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'task-id': task_id
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		task_status = r.json()
		task_status['status_code'] = r.status_code

		return task_status
