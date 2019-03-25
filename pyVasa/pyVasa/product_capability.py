import requests
import os
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class ProductCapability:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def details_product_capability(self):
		api_endpoint = '/api/rest/admin/product-capabilities'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		details = r.json()
		details['status_code'] = r.status_code

		return details

	def status_product_capability(self):
		api_endpoint = '/api/rest/admin/product-capabilities/server-status'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		status = r.json()
		status['status_code'] = r.status_code

		return status

	def enable_disable_vasa_provider(self, state=None, vp_password=None):
		api_endpoint = '/api/rest/admin/product-capabilities/vp'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'enableCapability': state,
			'password': vp_password
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		vp = r.json()
		vp['status_code'] = r.status_code

		return vp

	def enable_disable_sra(self, state=None, vp_password=None):
		api_endpoint = '/api/rest/admin/product-capabilities/sra'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'enableCapability': state,
			'password': vp_password
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		sra = r.json()
		sra['status_code'] = r.status_code

		return sra

	def restart_service(self, service=None):
		api_endpoint = '/api/rest/admin/product-capabilities/restart-service'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'service-type': service
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		serivce_restart = r.json()
		serivce_restart['status_code'] = r.status_code

		return serivce_restart
