#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from pyVasa.appliance_management import ApplianceManagement

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_appliance_management_logging_set

short_description: managing netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- set log level for a service type of netapp pyVasa appliance

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

  service:
    description:
    - select service type (accepted values - VP, SVC)
    required: true

  level:
    description:
    - select log level for VP or SVC (accepted values - INFO, ERROR, DEBUG, TRACE)
    required: true
'''

EXAMPLES = '''
 - name: "set log level for pyVasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_appliance_management_logging_set
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
     service: "{{ service_type }}"
     level: "{{ log_level }}"
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
			service=dict(required=True, type='str'),
			level=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	username = module.params['username']
	password = module.params['password']
	service = module.params['service']
	level = module.params['level']

	result = dict(changed=False)

	vp = ApplianceManagement(port=port, url=host, vp_user=username, vp_password=password)
	res = vp.set_logging(service_type=service, level=level)

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
