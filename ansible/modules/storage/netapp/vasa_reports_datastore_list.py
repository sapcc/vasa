#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.storage.netapp.vasa.reports import Reports
from ansible.module_utils.storage.netapp.vasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_reports_datastore_list

short_description: reports of netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- generate vsc datastores report of netapp pyVasa appliance


options:
  host:
    description:
    - The ip or name of the pyVasa unified appliance to manage.
    required: true

  port:
    description:
    - The port of the pyVasa unified appliance to manage.
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
'''

EXAMPLES = '''
 - name: "generate vsc datastores report of pyVasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_reports_datastore_list
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
'''

RETURN = '''
{
  "datastores": [
    {
      "freeCapacity": 0,
      "freePercentage": 0,
      "iops": 0,
      "latency": 0,
      "moRefType": "string",
      "moRefValue": "string",
      "name": "string",
      "totalCapacity": 0,
      "type": "string",
      "usedCapacity": 0,
      "usedPercentage": 0
    }
  ],
  "numOfRecords": 0,
  "responseMessage": "string",
  "timestamp": 0,
  "return_code": "int"
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vcenter_user=dict(required=True, type='str'),
			vcenter_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vcenter_user']
	vc_password = module.params['vcenter_password']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = Reports(
		port=port,
		url=host,
		token=token
	)

	res = vp.datastores()

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
