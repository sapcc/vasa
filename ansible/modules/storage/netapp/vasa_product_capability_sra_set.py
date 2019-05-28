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
module: vasa_product_capability_sra_set

short_description: product capabilities of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- enable/disable sra of netapp vasa appliance

options:
  host:
    description:
    - The ip or name of the vasa unified appliance to manage.
    required: true

  password:
    description:
    - vasa appliance password for login.
    required: true

  port:
    description:
    - The port of the vasa unified appliance to manage.
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

  state:
    description:
    - present checks ssh
    required: false
    default: 'present'
    choices: ['present', 'absent']
'''

EXAMPLES = '''
 - name: "enable/disable sra of netapp vasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_product_capability_sra_set
     host: "{{ inventory_hostname }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
     state: "{{ state | default('present') }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
'''

RETURN = '''
{
  "capabilityEnabled": true,
  "responseMessage": "string",
  "return_code": "int"
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			password=dict(required=True, type='str', no_log='true'),
			vcenter_user=dict(required=True, type='str'),
			vcenter_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			state=dict(default='present', choices=['present', 'absent'], type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	password = module.params['password']
	port = module.params['port']
	vc_user = module.params['vcenter_user']
	vc_password = module.params['vcenter_password']
	state = module.params['state']

	if state == 'absent':
		state = False
	elif state == 'present':
		state = True

	result = dict(changed=False)

	connect = VasaConnection(port=port, url=host, vcenter_user=vc_user, vcenter_password=vc_password)

	token = connect.new_token()

	vp = ProductCapability(port=port, url=host, token=token)

	res = vp.enable_disable_sra(vp_password=password, state=state)

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
