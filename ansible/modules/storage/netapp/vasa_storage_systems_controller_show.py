#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.storage.netapp.vasa.storage_systems import StorageSystems
from ansible.module_utils.storage.netapp.vasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_storage_systems_controller_show

short_description: storage systems of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- show storage controller details from vasa appliance

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

  controller_id:
    description:
    - id of the storage controller
    required: true
'''

EXAMPLES = '''
 - name: "show storage controller details from vasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_storage_systems_controller_show
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     controller_id: "{{ controller_id }}"
'''

RETURN = '''
{
  "numOfRecords": "string",
  "responseMessage": "string",
  "return_code": "int",
  "storageSystems": [
    {
      "clusterAdmin": true,
      "clusterNode": true,
      "clusterVServer": true,
      "discoveryInProgress": true,
      "id": "string",
      "ipAddress": "string",
      "name": "string",
      "parentController": "string",
      "partner": "string",
      "status": {
        "detail": "string",
        "reason": "string",
        "type": "string"
      },
      "supportedProtocols": [
        "string"
      ],
      "totalAllocated": 0,
      "totalCapacity": 0,
      "totalFree": 0,
      "totalUsed": 0,
      "type": "string",
      "userAddedSvm": true,
      "vaaiCapable": "string",
      "version": "string"
    }
  ]
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vc_user=dict(required=True, type='str'),
			vc_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			controller_id=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	controller_id = module.params['controller_id']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = StorageSystems(
		port=port,
		url=host,
		token=token
	)

	res = vp.list_storage_systems_by_controller(controller_id=controller_id)

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
