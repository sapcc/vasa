#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyVasa.storage_systems import StorageSystems
from pyVasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_storage_systems_add

short_description: storage systems of netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- add new storage system to netapp unified pyVasa appliance

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
 - name: "add new storage system to pyVasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_storage_systems_list
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     storage_ip: "{{ ip_of_new_storage }}"
     storage_user: "{{ storage_username }}"
     storage_pwd: "{{ storage_password }}"
     storage_port: "{{ storage_port }}"
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
			storage_ip=dict(required=True, type='str'),
			storage_user=dict(required=True, type='str'),
			storage_pwd=dict(required=True, type='str'),
			storage_port=dict(required=False, default='443'),
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	storage_ip = module.params['storage_ip']
	storage_user = module.params['storage_user']
	storage_pwd = module.params['storage_pwd']
	storage_port = module.params['storage_port']

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

	res = vp.add_storage_systems(
		ip_address=storage_ip,
		storage_user=storage_user,
		storage_pwd=storage_pwd,
		storage_port=storage_port
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
