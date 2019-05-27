#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.vsphere_privilege_validations import VspherePrivilegdeValidations
from pyvasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_vsphere_privilege_validations_show

short_description: vsphere privileges validation handling
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- show validation of privileges on vsphere

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

  priv_id:
    description:
    - privId from vcenter moref
    required: true
'''

EXAMPLES = '''
 - name: "show validation of privileges on vsphere"
   local_action:
     module: vasa_vsphere_privilege_validations_show
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     priv_id: "{{ privileges_id }}"
'''

RETURN = '''
{
  "morefToPrivilegesMap": {},
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
			priv_id=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vcenter_user']
	vc_password = module.params['vcenter_password']
	priv_id = module.params['priv_id']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = VspherePrivilegdeValidations(
		port=port,
		url=host,
		token=token
	)

	res = vp.show_privilidges(privilegeId=priv_id)

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
