#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule
from pyvasa.appliance_management import ApplianceManagement
from pyvasa.user_authentication import UserAuthentication

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_appliance_management_set_syslog

short_description: log management of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- create sys-log for netapp vasa appliance

options:
  host:
    description:
    - The ip or name of the vasa unified appliance to manage.
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

  hostname:
    description:
    - sys-log hostname
    required: true

  level:
    description:
    - select log level for VP or SVC (accepted values - INFO, ERROR, DEBUG, TRACE, WARN, FATAL, OFF and ALL)
    required: true

  pattern:
    description:
    - sys-log pattern (accepted values - "%d (%t) %-5p [%c{1}] - %m%n")
    required: true

  log_port:
    description:
    - sys-log port (acceptable port range is from 1 to 65535)
    required: true
'''

EXAMPLES = '''
 - name: "create sys-log for netapp vasa appliance"
   local_action:
     module: vasa_appliance_management_set_syslog
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     hostname: "{{ hostname }}"
     level: "{{ log_level }}"
     pattern: "{{ pattern }}"
     log_port: "{{ log_port }}"
'''

RETURN = '''
{
  "hostname": "string",
  "id": "string",
  "logLevel": "string",
  "pattern": "string",
  "port": "string",
  "responseMessage": "string",
  "return_code": "int"
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vc_user=dict(required=True, type='str'),
			vc_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default=8143),
			username=dict(required=True, type='str'),
			password=dict(required=True, type='str', no_log='true'),
			hostname=dict(required=True, type='str'),
			level=dict(required=True, type='str'),
			pattern=dict(required=True, type='str'),
			log_port=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	hostname = module.params['hostname']
	level = module.params['level']
	pattern = module.params['pattern']
	log_port = module.params['log_port']
	username = module.params['username']
	password = module.params['password']


	result = dict(changed=False)

	connect = UserAuthentication(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.login()
	token_id = token.get('vmwareApiSessionId')

	if not token_id:
		module.fail_json(msg="No Token!")

	vp = ApplianceManagement(
		port=port,
		url=host,
		vp_user=username,
		vp_password=password
	)

	res = vp.set_sys_log(
		token=token_id,
		host=hostname,
		level=level,
		pattern=pattern,
		log_port=log_port
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
		module.fail_json(msg=e.message)

	module.exit_json(**result)


main()
