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


class ExtentionManagement:
	def __init__(self, port=None, url=None, vp_user=None, vp_password=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/vsc"
		self.vasa_host = url

		if vp_user is not None:
			self.vp_user = vp_user

		if vp_password is not None:
			self.vp_password = vp_password

	def get_vsc_status(self):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'password': self.vp_password,
			'username': self.vp_user
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		vsc_details = r.json()
		vsc_details['status_code'] = r.status_code

		return vsc_details

	def register_vsc(self, vc_hostname=None, vc_user=None, vc_password=None, vc_port=None):
		url_action = self.url
		headers = {'Accept': 'application/json'}

		payload = {
			'vcenter': {
				'hostname': vc_hostname,
				'password': vc_password,
				'username': vc_user,
				'port': vc_port
			},
			'vsc_unified_appliance': {
				'hostname': self.vasa_host,
				'password': self.vp_password
			}
		}

		r = requests.post(url=url_action, headers=headers, json=payload, verify=False)

		register = r.json()
		register['status_code'] = r.status_code

		return register

	def unregister_vsc(self, vc_user=None, vc_password=None):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vcenter-password': vc_password,
			'vcenter-username': vc_user
		}

		r = requests.delete(url=url_action, headers=headers, verify=False)

		unregister = r.json()
		unregister['status_code'] = r.status_code

		return unregister
