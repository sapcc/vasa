import requests
import os
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class StorageSystems:
	def __init__(self, port=None, url=None, token=None):
		self.port = port
		self.url = "https://" + url

		if token is not None:
			self.token = token

	def list_storage_systems(self):
		api_endpoint = '/api/rest/admin/storage-systems'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		list_storage_sys = r.json()
		list_storage_sys['status_code'] = r.status_code

		return list_storage_sys

	def add_storage_systems(self, ip_address=None, storage_user=None, storage_pwd=None, storage_port=None):
		api_endpoint = '/api/rest/admin/storage-systems'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			"nameOrIpAddress": ip_address,
			"password": storage_pwd,
			"port": storage_port,
			"username": storage_user
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		add_storage = r.json()
		add_storage['status_code'] = r.status_code

		return add_storage

	def remove_storage_systems(self, controller_id=None):
		api_endpoint = '/api/rest/admin/storage-systems'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'controllerId': controller_id
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		rm_storage = r.json()
		rm_storage['status_code'] = r.status_code

		return rm_storage

	def list_aggregates(self, cluster_id=None):
		api_endpoint = '/api/rest/admin/'
		url_action = self.url + ":" + self.port + api_endpoint + cluster_id + '/aggregates'
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		list_aggregates = r.json()
		list_aggregates['status_code'] = r.status_code

		return list_aggregates

	def list_storage_systems_by_controller(self, controller_id=None):
		api_endpoint = '/api/rest/admin/storage-systems/'
		url_action = self.url + ":" + self.port + api_endpoint + controller_id
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		list_by_controller = r.json()
		list_by_controller['status_code'] = r.status_code

		return list_by_controller

	def list_flexvols(self, vserver=None):
		#ToDo - has remove since the last build
		api_endpoint = '/api/rest/admin/storage-systems/'
		url_action = self.url + ":" + self.port + api_endpoint + vserver + '/flexVols'
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		list_flexvols = r.json()
		list_flexvols['status_code'] = r.status_code

		return list_flexvols

	def show_flexvol_details(self, vserver=None, flexvol=None):
		# ToDo - has remove since the last build
		api_endpoint = '/api/rest/admin/storage-systems/'
		url_action = self.url + ":" + self.port + api_endpoint + vserver + '/flexVols/' + flexvol
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		flexvol_details = r.json()
		flexvol_details['status_code'] = r.status_code

		return flexvol_details

	def list_flexvol_by_scp(self, vserver=None, scp=None, protocol=None, cluster=None):
		api_endpoint = '/api/rest/admin/datastore/provisioning/flex-vols-scp'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'vserver-name': vserver,
			'cluster': cluster,
			'protocol': protocol,
			'scps': scp
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		flexvol_list = r.json()
		flexvol_list['status_code'] = r.status_code

		return flexvol_list

	def create_flexvol_by_scp(self, vserver=None, scp=None, aggr=None, cluster_ip=None, volume=None, size=None):
		api_endpoint = '/api/rest/admin/datastore/provisioning/flex-vols-scp'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}
		
		payload = {
			"clusterIp": cluster_ip,
			"flexibleVolume": {
				"aggrName": aggr,
				"profileName": scp,
				"sizeInMB": int(size),
				"volumeName": volume
			},
			"vServerName": vserver
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		flexvol_create = r.json()
		flexvol_create['status_code'] = r.status_code

		return flexvol_create

	def cluster_rediscover(self):
		api_endpoint = '/api/rest/admin/cluster/rediscover'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		rediscover = r.json()
		rediscover['status_code'] = r.status_code

		return rediscover
