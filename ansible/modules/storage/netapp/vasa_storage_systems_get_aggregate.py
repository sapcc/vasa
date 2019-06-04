#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.storage_systems import StorageSystems
from pyvasa.user_authentication import UserAuthentication

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_storage_systems_get_aggregate

short_description: storage systems of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- get details of a aggregate

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

  aggregate:
    description:
    - aggregate on storage cluster
    required: true
    
  cluster_id:
    description:
    - id of the storage cluster
    required: true
'''

EXAMPLES = '''
 - name: "get all aggregates and details"
   local_action:
     module: vasa_storage_systems_get_aggregate
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     aggregate: "{{ aggregate }}"
     cluster_id: "{{ cluster_id }}"
'''

RETURN = '''
{
  "aggregates": [
    {
      "freeCapacity": 0,
      "name": "string",
      "provisionedCapacity": 0,
      "status": "string",
      "usedCapacity": 0
    }
  ],
  "numOfRecords": 0,
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
			port=dict(required=False, default='8143'),
			aggregate=dict(required=True, type='str'),
			cluster_id=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	aggr = module.params['aggregate']
	cluster_id = module.params['cluster_id']

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

	vp = StorageSystems(
		port=port,
		url=host,
		token=token_id
	)

	res = vp.get_aggregate(
		cluster_id=cluster_id,
		aggregate=aggr
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
