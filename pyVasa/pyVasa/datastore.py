import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class Datastore:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/datastore"

		if token is not None:
			self.token = token

	def mount_datastore_on_host(self, container_id=None, ds_name=None, ds_type=None, host_id=None):
		api_endpoint = "/mount-on-host"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'containerId': container_id,
			'datastoreName': ds_name,
			'datastoreType': ds_type,
			'hostMoref': host_id
			}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		mount = r.json()
		mount['status_code'] = r.status_code

		return mount

	def mount_datastore_on_additional_hosts(self, ds_name=None, ds_type=None, host_ids=None):
		api_endpoint = "/mount-on-additional-hosts"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'datastoreName': ds_name,
			'datastoreType': ds_type,
			'hostMoref': [
				host_ids
			]
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		mounts = r.json()
		mounts['status_code'] = r.status_code

		return mounts

	def unmount_datastore(self, ds_name=None, ds_type=None, host_ids=None):
		api_endpoint = "/unmount"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'datastoreName': ds_name,
			'datastoreType': ds_type,
			'hostMoref': [
				host_ids
			]
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		mounts = r.json()
		mounts['status_code'] = r.status_code

		return mounts

	def create_datastore(self, cluster_ip=None, ds_type=None, scp=None, description=None, flexvol=None,
	                     ds_name=None, protocol=None, target=None, vserver=None):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			"clusterIp": cluster_ip,
			"dataStoreType": ds_type,
			"defaultSCP": scp,
			"description": description,
			"flexVolSCPMap": {
				flexvol
			},
			"name": ds_name,
			"protocol": protocol,
			"targetMoref": target,
			"vserverName": vserver
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		ds_create = r.json()
		ds_create['status_code'] = r.status_code

		return ds_create

	def delete_datastore(self, ds_type=None, ds_moref=None):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'datastore-type': ds_type,
			'datastore-moref': ds_moref
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		ds_delete = r.json()
		ds_delete['status_code'] = r.status_code

		return ds_delete

	def get_datastore(self, ds_type=None, ds_name=None):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'datastore-type': ds_type,
			'name': ds_name
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ds_details = r.json()
		ds_details['status_code'] = r.status_code

		return ds_details

	def get_datastore_clusters(self, scp=None, protocol=None):
		api_endpoint = "/clusters"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'profile-names': scp,
			'protocol': protocol
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ds_cfilter = r.json()
		ds_cfilter['status_code'] = r.status_code

		return ds_cfilter

	def get_aggregates_for_scp(self, scp=None, cluster=None, vserver=None):
		api_endpoint = "/provisioning/aggregates/forscp"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'profile-names': scp,
			'cluster': cluster,
			'vserver-name': vserver
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ds_afilter = r.json()
		ds_afilter['status_code'] = r.status_code

		return ds_afilter

	def add_storage(self, ds_type=None, ds_name=None, cluster_ip=None, scp=None, volume=None, vserver=None):
		api_endpoint = "/storage"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'datastore-type': ds_type
		}

		payload = {
			"clusterIP": cluster_ip,
			"datastoreName": ds_name,
			"flexVolSCPNames": [
				{
					"flexVolName": volume,
					"scpName": scp
				}
			],
			"vserverName": vserver
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		s_add = r.json()
		s_add['status_code'] = r.status_code

		return s_add

	def delete_storage(self, ds_type=None, ds_name=None, volume=None):
		api_endpoint = "/storage"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'datastore-name': ds_name,
			'datastore-type': ds_type,
			'flex-vol-names': volume
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		s_rm = r.json()
		s_rm['status_code'] = r.status_code

		return s_rm
