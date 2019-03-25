import requests
import os
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class ApplianceManagement:
	def __init__(self, port=None, url=None, vp_user=None, vp_password=None):
		self.port = port
		self.url = "https://" + url
		self.vp_user = vp_user
		self.vp_password = vp_password

	def status_ssh_management_appliance(self):
		api_endpoint = '/api/rest/appliance/management/ssh'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ssh_status = r.json()
		ssh_status['status_code'] = r.status_code

		return ssh_status

	def enable_ssh_management_appliance(self):
		api_endpoint = '/api/rest/appliance/management/ssh/enable'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		ssh_enable = r.json()
		ssh_enable['status_code'] = r.status_code

		return ssh_enable

	def disable_ssh_management_appliance(self):
		api_endpoint = '/api/rest/appliance/management/ssh/disable'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		ssh_disable = r.json()
		ssh_disable['status_code'] = r.status_code

		return ssh_disable

	def list_appliance_details(self):
		api_endpoint = '/api/rest/appliance/management/appliance-details'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		details = r.json()
		details['status_code'] = r.status_code

		return details

	def list_network_settings(self):
		api_endpoint = '/api/rest/appliance/management/network-settings'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		nw_settings = r.json()
		nw_settings['status_code'] = r.status_code

		return nw_settings

	def modify_network_settings(self, dns_server=None, gw=None, ip=None, ip_family=None, mode=None, nmask=None):
		api_endpoint = '/api/rest/appliance/management/network-settings'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		payload = {
			"dnsServers": [
				dns_server
				],
			"gateway": gw,
			"ip": ip,
			"ipFamily": ip_family,
			"mode": mode,
			"netmask": nmask
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		nw_modify = r.json()
		nw_modify['status_code'] = r.status_code

		return nw_modify

	def list_ntp_server(self):
		api_endpoint = '/api/rest/appliance/management/ntp-server'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ntp_server = r.json()
		ntp_server['status_code'] = r.status_code

		return ntp_server

	def set_ntp_server(self, skip_refresh=None, ntp_server=None):
		api_endpoint = '/api/rest/appliance/management/ntp-server'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'ntpserver': ntp_server,
			'skip-refresh': skip_refresh
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		ntp = r.json()
		ntp['status_code'] = r.status_code

		return ntp

	def create_support_bundle(self):
		api_endpoint = '/api/rest/appliance/management/support-bundle'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		bundle = r.json()
		bundle['status_code'] = r.status_code

		return bundle

	def available_time_zones(self):
		api_endpoint = '/api/rest/appliance/management/available-time-zones'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		timezones = r.json()
		timezones['status_code'] = r.status_code

		return timezones

	def show_timezone(self):
		api_endpoint = '/api/rest/appliance/management/time-zone'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		timezone_show = r.json()
		timezone_show['status_code'] = r.status_code

		return timezone_show

	def set_timezone(self, timezone=None):
		api_endpoint = '/api/rest/appliance/management/time-zone'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'timezone': timezone
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		timezone = r.json()
		timezone['status_code'] = r.status_code

		return timezone

	def show_logging(self, service_type=None):
		api_endpoint = '/api/rest/appliance/management/logging'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'service-type': service_type
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		logging = r.json()
		logging['status_code'] = r.status_code

		return logging

	def set_logging(self, service_type=None, level=None):
		api_endpoint = '/api/rest/appliance/management/logging'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'log-level': level,
			'service-type': service_type
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		log_level = r.json()
		log_level['status_code'] = r.status_code

		return log_level

	def reset_password(self, user=None, old_pw=None, new_pw=None):
		api_endpoint = '/api/rest/appliance/management/password/reset'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'reset-user': user,
			'old-password': old_pw,
			'new-password': new_pw
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		pw_reset = r.json()
		pw_reset['status_code'] = r.status_code

		return pw_reset

	def ping_host(self, hostname=None):
		api_endpoint = '/api/rest/appliance/management/network-settings/ping-host'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'hostname': hostname
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ping = r.json()
		ping['status_code'] = r.status_code

		return ping

	def show_route(self):
		api_endpoint = '/api/rest/appliance/management/network-settings/static-route'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		route_show = r.json()
		route_show['status_code'] = r.status_code

		return route_show

	def add_route(self, host=None, gateway=None):
		api_endpoint = '/api/rest/appliance/management/network-settings/static-route'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'host': host,
			'gateway': gateway
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		route_add = r.json()
		route_add['status_code'] = r.status_code

		return route_add

	def delete_route(self, host=None, gateway=None):
		api_endpoint = '/api/rest/appliance/management/network-settings/static-route'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'host': host,
			'gateway': gateway
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		route_delete = r.json()
		route_delete['status_code'] = r.status_code

		return route_delete

	def show_certificate(self, service_type=None):
		api_endpoint = '/api/rest/appliance/management/certificate'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			#'Accept': accept,
			'service-type': service_type
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		cert_show = r.json()
		cert_show['status_code'] = r.status_code

		return cert_show

	def import_certificate(self, service_type=None, certificate=None):
		api_endpoint = '/api/rest/appliance/management/certificate'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'service-type': service_type
		}

		payload = {
			"certificateChain": [
				certificate
			]
		}

		r = requests.put(url=url_action, headers=headers, json=payload, verify=False)

		cert_import = r.json()
		cert_import['status_code'] = r.status_code

		return cert_import

	def generate_certificate(self, service_type=None):
		api_endpoint = '/api/rest/appliance/management/certificate/generate-csr'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'service-type': service_type
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		generate_cert = r.json()
		generate_cert['status_code'] = r.status_code

		return generate_cert

	def reset_certificate(self, service_type=None):
		api_endpoint = '/api/rest/appliance/management/certificate/reset'
		url_action = self.url + ":" + self.port + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user,
			'service-type': service_type
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		reset_cert = r.json()
		reset_cert['status_code'] = r.status_code

		return reset_cert
