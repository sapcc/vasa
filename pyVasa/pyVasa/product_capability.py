#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

import requests
import os
from builtins import object
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""


class ProductCapability(object):
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port + "/" + self.api
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/product-capabilities"

		if token is not None:
			self.token = token

	def get_product_capabilities(self):
		url_action = self.url
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		details = r.json()
		details['status_code'] = r.status_code

		return details

	def get_server_status(self):
		api_endpoint = "/server-status"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		status = r.json()
		status['status_code'] = r.status_code

		return status

	def set_vp_status(self, state=None, vp_password=None):
		api_endpoint = "/vp"
		url_action = self.url + api_endpoint
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

	def set_sra_status(self, state=None, vp_password=None):
		api_endpoint = "/sra"
		url_action = self.url + api_endpoint
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
		api_endpoint = "/restart-service"
		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token,
			'service-type': service
		}

		r = requests.put(url=url_action, headers=headers, verify=False)

		serivce_restart = r.json()
		serivce_restart['status_code'] = r.status_code

		return serivce_restart
