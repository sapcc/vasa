import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class StorageSystems:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port + "/" + self.api
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/storage-systems"

		if token is not None:
			self.token = token

	def get_storage_systems(self):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		get_storage_sys = r.json()
		get_storage_sys['status_code'] = r.status_code

		return get_storage_sys

	def add_storage_system(self, ip_address=None, storage_user=None, storage_pwd=None, storage_port=None):
		url_action = self.url
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

	def delete_storage_system(self, controller_id=None):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'controllerId': controller_id
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		del_storage = r.json()
		del_storage['status_code'] = r.status_code

		return del_storage

	def get_aggregate(self, cluster_id=None, aggregate=None):
		api_endpoint = "/" + cluster_id + "/aggregate"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'aggregateName': aggregate
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		aggregate = r.json()
		aggregate['status_code'] = r.status_code

		return aggregate

	def get_aggregates(self, cluster_id=None):
		api_endpoint = "/" + cluster_id + "/aggregates"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		aggregates = r.json()
		aggregates['status_code'] = r.status_code

		return aggregates

	def get_cluster(self, cluster_id=None):
		api_endpoint = "/" + cluster_id
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		cluster = r.json()
		cluster['status_code'] = r.status_code

		return cluster

	def get_flexvols(self, vserver=None, scp=None, protocol=None, cluster=None):
		api_endpoint = "/provisioning/flex-vols"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'vserver-name': vserver,
			'cluster': cluster,
			'protocol': protocol,
			'scps': scp
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		flexvols = r.json()
		flexvols['status_code'] = r.status_code

		return flexvols

	def create_flexvol(self, vserver=None, scp=None, aggr=None, cluster_ip=None, volume=None, size=None):
		api_endpoint = "/provisioning/flex-vols"
		url_action = self.url + api_endpoint
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
		api_endpoint = "/rediscover"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		rediscover = r.json()
		rediscover['status_code'] = r.status_code

		return rediscover
