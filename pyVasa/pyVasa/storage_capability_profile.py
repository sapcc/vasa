import requests
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class StorageCapability:
	def __init__(self, port=None, url=None, vp_user=None, vp_password=None, token=None):
		self.port = port
		self.url = "https://" + url
		self.vp_user = vp_user
		self.vp_password = vp_password

		if token is not None:
			self.token = token

	def list_storage_capability_profile(self):
		api_endpoint = '/api/rest/admin/storage-capabilities'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		list_profiles = r.json()
		list_profiles['status_code'] = r.status_code

		return list_profiles

	def create_storage_capability_profile(self, profile_name=None,
	                                      description=None, qos=None,
	                                      compression=None, deduplication=None,
	                                      encryption=None, iops=None,
	                                      platform=None, space_efficiency=None,
	                                      tiering_policy=None):

		api_endpoint = '/api/rest/admin/storage-capabilities'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			'name': profile_name,
			'description': description,
			'capabilities': {
				'adaptiveQoS': qos,
				'compression': compression,
				'deduplication': deduplication,
				'encryption': encryption,
				'maxThroughputIops': iops,
				'platformType': platform,
				'spaceEfficiency': space_efficiency,
				'tieringPolicy': tiering_policy
				}
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		create_profile = r.json()
		create_profile['status_code'] = r.status_code

		return create_profile

	def update_storage_capability_profile(self, profile_name=None,
	                                      description=None, qos=None,
	                                      compression=None, deduplication=None,
	                                      encryption=None, iops=None,
	                                      platform=None, space_efficiency=None,
	                                      tiering_policy=None, profile_id=None):

		api_endpoint = '/api/rest/admin/storage-capabilities'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		#TODO
		# ''' Difference naming of profile name in method put '''
		payload = {
			'storageCapabilityProfile': {
				'name': profile_name,
				'description': description,
				'id': profile_id,
				'capabilities': {
					'adaptiveQoS': qos,
					'compression': compression,
					'deduplication': deduplication,
					'encryption': encryption,
					'maxThroughputIops': iops,
					'platformType': platform,
					'spaceEfficiency': space_efficiency,
					'tieringPolicy': tiering_policy
					}
			}
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		update_profile = r.json()
		update_profile['status_code'] = r.status_code

		return update_profile

	def delete_storage_capability_profile(self, profile_name=None):
		api_endpoint = '/api/rest/admin/storage-capabilities'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'profile-name': profile_name
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		delete_profiles = r.json()
		delete_profiles['status_code'] = r.status_code

		return delete_profiles

	def delete_storage_capability_profile_id(self, profile_id=None):
		api_endpoint = '/api/rest/admin/storage-capabilities/'
		url_action = self.url + ":" + self.port + api_endpoint + profile_id
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		delete_profile_id = r.json()
		delete_profile_id['status_code'] = r.status_code

		return delete_profile_id

	def show_storage_capability_profile_id(self, profile_id=None):
		api_endpoint = '/api/rest/admin/storage-capabilities/'
		url_action = self.url + ":" + self.port + api_endpoint + profile_id
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		show_profile_id = r.json()
		show_profile_id['status_code'] = r.status_code

		return show_profile_id

	def clone_storage_capability_profile(self, profile_name=None,
	                                     description=None, qos=None,
	                                     compression=None, deduplication=None,
	                                     encryption=None, iops=None,
	                                     platform=None, space_efficiency=None,
	                                     tiering_policy=None, profile_id=None,
	                                     new_profile_name=None):

		api_endpoint = '/api/rest/admin/storage-capabilities/clone'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		payload = {
			"baseProfileName": profile_name,
			"storageCapabilityProfile": {
				"capabilities": {
					"adaptiveQoS": qos,
					"compression": compression,
					"deduplication": deduplication,
					"encryption": encryption,
					"maxThroughputIops": iops,
					"platformType": platform,
					"spaceEfficiency": space_efficiency,
					"tieringPolicy": tiering_policy
					},
				"description": description,
				"id": profile_id,
				"name": new_profile_name
				}
			}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		clone_profile = r.json()
		clone_profile['status_code'] = r.status_code

		return clone_profile

	def list_storage_capability_profile_names(self):
		api_endpoint = '/api/rest/admin/storage-capabilities/profile-names'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		show_profile_id = r.json()
		show_profile_id['status_code'] = r.status_code

		return show_profile_id
