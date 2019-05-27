#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from pyvasa.appliance_management import ApplianceManagement

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_appliance_management_network_modify

short_description: managing netapp pyvasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- modify network settings of pyvasa appliance

options:
  host:
    description:
    - The ip or name of the pyvasa unified appliance to manage.
    required: true

  username:
    description:
    - pyvasa appliance username for login.
    required: true

  password:
    description:
    - pyvasa appliance password for login.
    required: true

  port:
    description:
    - The port of the pyvasa unified appliance to manage.
    required: false
    default: '8143'

  dns_server:
    description:
    - list of dns_server
    required: true

  gateway:
    description:
    - gateway for pyvasa appliance
    required: true

  ip_address:
    description:
    - ip address of pyvasa appliance
    required: true

  ip_family:
    description:
    - IPV4 or IPV6 ip address family (accapted values - IPV4, IPV6)
    required: true

  mode:
    description:
    - mode for ip address (accapted values - STATIC, DYNAMIC)
    required: true

  netmask:
    description:
    - netmask of pyvasa appliance
    required: true
'''

EXAMPLES = '''
 - name: "modify network settings of pyvasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_appliance_management_network_modify
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
     dns_server: "{{ dns_server }}"
     gateway: "{{ gateway }}"
     ip_address: "{{ ip_address }}"
     ip_family: "{{ ip_family }}"
     mode: "{{ mode }}"
     netmask: "{{ netmask }}"
'''

RETURN = '''
{
  "responseMessage": "string",
  "return_code": "int"
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			username=dict(required=True, type='str'),
			password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			dns_server=dict(required=True, type='str'),
			gateway=dict(required=True, type='str'),
			ip_address=dict(required=True, type='str'),
			ip_family=dict(required=True, type='str'),
			mode=dict(required=True, type='str'),
			netmask=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	username = module.params['username']
	password = module.params['password']
	dns_server = module.params['dns_server']
	gw = module.params['gateway']
	ip = module.params['ip_address']
	ip_family = module.params['ip_family']
	mode = module.params['mode']
	nmask = module.params['netmask']

	result = dict(changed=False)

	vp = ApplianceManagement(
		port=port,
		url=host,
		vp_user=username,
		vp_password=password
	)

	res = vp.modify_network_settings(
		dns_server=dns_server,
		gw=gw,
		ip=ip,
		ip_family=ip_family,
		mode=mode,
		nmask=nmask
	)

	try:
		if res['status_code'] == 200:
			result.update(result=res)
			result.update(changed=True)
		else:
			result.update(result=res)
			result.update(changed=False)
			result.update(failed=True)

	except BaseException as e:
		module.fail_json(message=e.message)

	module.exit_json(**result)


main()
