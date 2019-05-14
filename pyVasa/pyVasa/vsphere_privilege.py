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


class VspherePrivilege:
	def __init__(self, port=None, url=None, token=None, api_version='1.0'):
		self.api = api_version
		self.port = port
		self.url = "https://" + url + ":" + self.port + "/api/rest/" + self.api + "/vcenter/"

		if token is not None:
			self.token = token

	def get_vcenter_privileges(self, privilegeId=None, moref=None):
		if privilegeId and moref:
			raise BaseException("Please user moref OR privilegeId not both!")

		if privilegeId:
			api_endpoint = "privileges/?privilegeId=" + privilegeId + "privileges/?moref=" + moref

		if moref:
			# ToDo moref doesn't work. Address issue to NetApp.
			api_endpoint = "privileges/?moref=" + moref

		url_action = self.url + api_endpoint
		headers = {
			'Accept': 'application/json',
			'vmware-api-session-id': self.token
		}

		r = requests.get(url=url_action, headers=headers, verify=False)

		priv_details = r.json()
		priv_details['status_code'] = r.status_code

		return priv_details
