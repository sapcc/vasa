#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from pyVasa.manage_extentions import ManageExtentions

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_manage_extentions_vsc_register

short_description: manage extentions of netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- register netapp VSC pyVasa appliance to vcenter

options:
  host:
    description:
    - The ip or name of the pyVasa unified appliance to manage.
    required: true

  username:
    description:
    - pyVasa appliance username for login.
    required: true

  password:
    description:
    - pyVasa appliance password for login.
    required: true

  port:
    description:
    - The port of the pyVasa unified appliance to manage.
    required: false
    default: '8143'

  vc_port:
    description:
    - vcenter port
    required: false
    default: '443'

  vc_user:
    description:
    - vcenter username
    required: true

  vc_password:
    description:
    - vcenter user password
    required: true

  vc_hostname:
    description:
    - vcenter hostname or ip
    required: true
'''

EXAMPLES = '''
 - name: "register VSC pyVasa appliance {{ inventory_hostname }} to vcenter"
   local_action:
     module: vasa_manage_extentions_register
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
     vc_port: "{{ vcenter_port }}"
     vc_hostname: "{{ vcenter_hostname or vcenter_ip }}"
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
			username=dict(required=True, type='str'),
			password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			vc_hostname=dict(required=True, type='str'),
			vc_user=dict(required=True, type='str'),
			vc_password=dict(required=True, type='str', no_log='true'),
			vc_port=dict(required=False, default='443')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	username = module.params['username']
	password = module.params['password']
	port = module.params['port']
	vc_hostname = module.params['vc_hostname']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	vc_port = module.params['vc_port']

	result = dict(changed=False)

	vp = ManageExtentions(port=port, url=host, vp_user=username, vp_password=password)

	res = vp.register_vsc(
		vc_hostname=vc_hostname,
		vc_user=vc_user,
		vc_password=vc_password,
		vc_port=vc_port
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
