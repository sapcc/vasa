#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class ApplianceManagement(object):
	def __init__(self, port=None, url=None, vp_user=None, vp_password=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/appliance/management/"
		self.vp_user = vp_user
		self.vp_password = vp_password

	def get_ssh_status(self):
		api_endpoint = "ssh"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		ssh_status = r.json()
		ssh_status['status_code'] = r.status_code

		return ssh_status

	def set_ssh_enable(self):
		api_endpoint = "ssh/enable"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		ssh_enable = r.json()
		ssh_enable['status_code'] = r.status_code

		return ssh_enable

	def set_ssh_disable(self):
		api_endpoint = "ssh/disable"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		ssh_disable = r.json()
		ssh_disable['status_code'] = r.status_code

		return ssh_disable

	def get_appliance_details(self):
		api_endpoint = "appliance-details"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		details = r.json()
		details['status_code'] = r.status_code

		return details

	def get_network_settings(self):
		api_endpoint = "network-settings"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		nw_settings = r.json()
		nw_settings['status_code'] = r.status_code

		return nw_settings

	def set_network_settings(self, dns_server=None, gw=None, ip=None, ip_family=None, mode=None, nmask=None):
		api_endpoint = "network-settings"
		url_action = self.url + api_endpoint
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

		set_nw = r.json()
		set_nw['status_code'] = r.status_code

		return set_nw

	def get_ntp_server(self):
		api_endpoint = "ntp-server"
		url_action = self.url + api_endpoint
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
		api_endpoint = "ntp-server"
		url_action = self.url + api_endpoint
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
		api_endpoint = "support-bundle"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.post(url=url_action, headers=headers, verify=False)

		bundle = r.json()
		bundle['status_code'] = r.status_code

		return bundle

	def get_time_zones(self):
		api_endpoint = "available-time-zones"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		timezones = r.json()
		timezones['status_code'] = r.status_code

		return timezones

	def get_time_zone(self):
		api_endpoint = "time-zone"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		timezone_show = r.json()
		timezone_show['status_code'] = r.status_code

		return timezone_show

	def set_time_zone(self, timezone=None):
		api_endpoint = "time-zone"
		url_action = self.url + api_endpoint
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

	def get_logging(self, service_type=None):
		api_endpoint = "logging"
		url_action = self.url + api_endpoint
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
		api_endpoint = "logging"
		url_action = self.url + api_endpoint
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

	def set_password(self, user=None, old_pw=None, new_pw=None):
		api_endpoint = "password/reset"
		url_action = self.url + api_endpoint
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
		api_endpoint = "network-settings/ping-host"
		url_action = self.url + api_endpoint
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

	def get_static_route(self):
		api_endpoint = "network-settings/static-route"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		route_show = r.json()
		route_show['status_code'] = r.status_code

		return route_show

	def set_static_route(self, host=None, gateway=None):
		api_endpoint = "network-settings/static-route"
		url_action = self.url + api_endpoint
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

	def delete_static_route(self, host=None, gateway=None):
		api_endpoint = "network-settings/static-route"
		url_action = self.url + api_endpoint
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

	def get_certificate(self, service_type=None):
		api_endpoint = "certificate"
		url_action = self.url + api_endpoint
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

	def set_certificate(self, service_type=None, certificate=None):
		api_endpoint = "certificate"
		url_action = self.url + api_endpoint
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

	def generate_csr(self, service_type=None):
		api_endpoint = "certificate/generate-csr"
		url_action = self.url + api_endpoint
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
		api_endpoint = "certificate/reset"
		url_action = self.url + api_endpoint
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

	def update_sys_log(self, uuid=None, host=None, level=None, pattern=None, log_port=None, token=None):
		api_endpoint = "log-config/sys-log"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': token,
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

	def set_sys_log(self, host=None, level=None, pattern=None, log_port=None, token=None):
		api_endpoint = "log-config/sys-log"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': token
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

	def get_sys_log(self, uuid=None, token=None):
		api_endpoint = "log-config/sys-log"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': token,
			'uuid': uuid
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		syslog_details = r.json()
		syslog_details['status_code'] = r.status_code

		return syslog_details

	def delete_sys_log(self, uuid=None, token=None):
		api_endpoint = "log-config/sys-log"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': token,
			'uuid': uuid
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		syslog_del = r.json()
		syslog_del['status_code'] = r.status_code

		return syslog_del