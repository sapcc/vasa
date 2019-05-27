#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.product_capability import ProductCapability
from pyvasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_product_capability_service_restart

short_description: product capabilities of netapp pyvasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- restart service of netapp pyvasa appliance

options:
  host:
    description:
    - The ip or name of the pyvasa unified appliance to manage.
    required: true

  port:
    description:
    - The port of the pyvasa unified appliance to manage.
    required: false
    default: '8143'

  vc_user:
    description:
    - vcenter username
    required: true

  vc_password:
    description:
    - vcenter user password
    required: true

  service:
    description:
    - select service type (accepted values - VP, VSC, ALL)
    required: true
'''

EXAMPLES = '''
 - name: "restart service of netapp pyvasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_product_capability_service_restart
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     service: "{{ service_type }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
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
			vcenter_user=dict(required=True, type='str'),
			vcenter_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			service=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vcenter_user']
	vc_password = module.params['vcenter_password']
	service = module.params['service']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = ProductCapability(
		port=port,
		url=host,
		token=token
	)

	res = vp.restart_service(
		service=service
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
