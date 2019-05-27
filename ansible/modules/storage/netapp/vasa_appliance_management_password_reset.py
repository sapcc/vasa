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
module: vasa_appliance_management_password_reset

short_description: managing netapp pyvasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description: reset the password for maint/administration user of pyvasa appliance

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

  user:
    description:
    - select user (accepted values - maint, administrator)
    required: True

  old_pw:
    description:
    - old user password
    required: True

  new_pw:
    description:
    - new user password
    required: True
'''

EXAMPLES = '''
 - name: "reset the password for maint/administration user of pyvasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_appliance_management_password_reset
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
     user: "{{ maint or administrator }}"
     old_pw: "{{ old_password }}"
     new_pw: "{{ new_password }}"
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
			user=dict(required=True, type='str'),
			old_pw=dict(required=True, type='str', no_log='true'),
			new_pw=dict(required=True, type='str', no_log='true')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	username = module.params['username']
	password = module.params['password']
	user = module.params['user']
	old_pw = module.params['old_pw']
	new_pw = module.params['new_pw']

	result = dict(changed=False)

	vp = ApplianceManagement(port=port, url=host, vp_user=username, vp_password=password)
	res = vp.reset_password(user=user, old_pw=old_pw, new_pw=new_pw)

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
