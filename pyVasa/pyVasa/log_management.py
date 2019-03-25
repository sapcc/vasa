import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class LogManagement:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def syslog_modify(self, uuid=None, host=None, level=None, pattern=None, log_port=None):
		api_endpoint = '/api/rest/admin/appliance-management/log-config/sys-log'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'uuid': uuid
		}

		payload = {
			"hostname": host,
			"logLevel": level,
			"pattern": pattern,
			"port": log_port
			}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		syslog_modify = r.json()
		syslog_modify['status_code'] = r.status_code

		return syslog_modify

	def syslog_create(self, host=None, level=None, pattern=None, log_port=None):
		api_endpoint = '/api/rest/admin/appliance-management/log-config/sys-log'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			"hostname": host,
			"logLevel": level,
			"pattern": pattern,
			"port": log_port
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		syslog_set = r.json()
		syslog_set['status_code'] = r.status_code

		return syslog_set

	def syslog_details(self, uuid=None):
		api_endpoint = '/api/rest/admin/appliance-management/log-config/sys-log'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'uuid': uuid
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		syslog_details = r.json()
		syslog_details['status_code'] = r.status_code

		return syslog_details

	def syslog_delete(self, uuid=None):
		api_endpoint = '/api/rest/admin/appliance-management/log-config/sys-log'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'uuid': uuid
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		syslog_del = r.json()
		syslog_del['status_code'] = r.status_code

		return syslog_del
