#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.storage_capability_profile import StorageCapabilityProfile
from pyvasa.user_authentication import UserAuthentication

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_storage_capability_profile_create

short_description: storage capabilities of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- create a storage capabilitiy profile for the netapp unified vasa appliance

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

  profile_name:
    description:
    - name of the storage capability profile
    required: true

  description:
    description:
    - description
    required: true

  qos:
    description:
    - adaptive qos (accepted values - VALUE, PERFORMANCE, EXTREME)
    required: true

  compression:
    description:
    - storage compression
    required: true

  deduplication:
    description:
    - storage deduplication
    required: true

  encryption:
    description:
    - storage encryption
    required: true

  iops:
    description:
    - storage max throughput iops
    required: true

  platform:
    description:
    - netapp hardware platform (accepted values - FAS, AFF)
    required: true

  space_efficiency:
    description:
    - storage space efficiency (accepted values - Thick, Thin)
    required: true

  tiering_policy:
    description:
    - storage tiering policy
    required: true
'''

EXAMPLES = '''
 - name: "create a storage capabilitiy profile of vasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_storage_capability_profile_create
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     profile_name: "{{ new_profile_name  }}"
     description: "{{ descripe_your_profile }}"
     qos: "{{ type_of_qos }}"
     compression: "{{ enable/disable }}"
     deduplication: "{{ enable/disable }}"
     encryption: "{{ enable/disable }}"
     iops: "{{ io_operations }}"
     platform: "{{ netapp_hardware_type }}"
     space_efficiency: "{{ thin_or_thick }}"
     tiering_policy: "{{ policy }}"
'''

RETURN = '''
{
  "datastoreCapabilityProfile": {
    "capabilities": {
      "adaptiveQoS": "string",
      "compression": true,
      "deduplication": true,
      "encryption": true,
      "maxThroughputIops": 0,
      "platformType": "string",
      "spaceEfficiency": "string",
      "tieringPolicy": "string"
    },
    "description": "string",
    "id": 0,
    "name": "string"
  },
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
			profile_name=dict(required=True, type='str'),
			description=dict(required=True, type='str'),
			qos=dict(required=True, type='str'),
			compression=dict(required=True, type='bool'),
			deduplication=dict(required=True, type='bool'),
			encryption=dict(required=True, type='bool'),
			iops=dict(required=True, type='str'),
			platform=dict(required=True, type='str'),
			space_efficiency=dict(required=True, type='str'),
			tiering_policy=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	profile_name = module.params['profile_name']
	description = module.params['description']
	qos = module.params['qos']
	compression = module.params['compression']
	deduplication = module.params['deduplication']
	encryption = module.params['encryption']
	iops = module.params['iops']
	platform = module.params['platform']
	space_efficiency = module.params['space_efficiency']
	tiering_policy = module.params['tiering_policy']

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

	vp = StorageCapabilityProfile(
		port=port,
		url=host,
		token=token_id
	)

	res = vp.create_storage_capability_profile(
		profile_name=profile_name,
		description=description,
		qos=qos,
		compression=compression,
		deduplication=deduplication,
		encryption=encryption,
		iops=iops,
		platform=platform,
		space_efficiency=space_efficiency,
		tiering_policy=tiering_policy
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
