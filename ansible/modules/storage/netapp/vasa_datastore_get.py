#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule

from pyvasa.datastore import Datastore
from pyvasa.user_authentication import UserAuthentication

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_datastore_get

short_description: datastore handle of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- show details of a datastore container on vcenter

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

  ds_type:
    description:
    - type of the datastore
    required: false
    default: 'VVOL'

  ds_name:
    description:
    - name of the datastore
    required: false
'''

EXAMPLES = '''
 - name: "show details of a datastore on vcenter"
   local_action:
     module: vasa_datastore_get
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     ds_type: "{{ datastore_type }}"
     ds_name: "{{ datastore_name }}"
'''

RETURN = '''
{
  "datastoresList": [
    {
      "datastoreMoref": "string",
      "defaultDatastoreCapabilityProfileId": 0,
      "description": "string",
      "flexvols": [
        {
          "aggrName": "string",
          "aggregateUuid": "string",
          "autoGrowEnabled": true,
          "compressionEnabled": true,
          "dedupeEnabled": true,
          "encryptionEnabled": true,
          "failedReason": "string",
          "hosedValue": 0,
          "id": "string",
          "junctionPath": "string",
          "moving": true,
          "name": "string",
          "qosPolicyGroup": "string",
          "root": true,
          "sizeAvailable": 0,
          "sizeTotal": 0,
          "sizeUsed": 0,
          "spaceGuarentee": "string",
          "state": "string",
          "storageController": {
            "controllerId": 0,
            "controllerIp": "string",
            "id": "string",
            "name": "string",
            "typeStr": "string",
            "uri": {
              "absolute": true,
              "authority": "string",
              "fragment": "string",
              "host": "string",
              "opaque": true,
              "path": "string",
              "port": 0,
              "query": "string",
              "rawAuthority": "string",
              "rawFragment": "string",
              "rawPath": "string",
              "rawQuery": "string",
              "rawSchemeSpecificPart": "string",
              "rawUserInfo": "string",
              "scheme": "string",
              "schemeSpecificPart": "string",
              "userInfo": "string"
            },
            "vcenterServerUuid": "string"
          },
          "tieringPolicy": "string",
          "type": "string",
          "typeStr": "string",
          "uri": {
            "absolute": true,
            "authority": "string",
            "fragment": "string",
            "host": "string",
            "opaque": true,
            "path": "string",
            "port": 0,
            "query": "string",
            "rawAuthority": "string",
            "rawFragment": "string",
            "rawPath": "string",
            "rawQuery": "string",
            "rawSchemeSpecificPart": "string",
            "rawUserInfo": "string",
            "scheme": "string",
            "schemeSpecificPart": "string",
            "userInfo": "string"
          },
          "uuid": "string",
          "vcenterServerUuid": "string"
        }
      ],
      "hostMorefs": [
        "string"
      ],
      "id": "string",
      "name": "string",
      "protocol": "string",
      "scpNames": [
        "string"
      ],
      "typeStr": "string",
      "uri": {
        "absolute": true,
        "authority": "string",
        "fragment": "string",
        "host": "string",
        "opaque": true,
        "path": "string",
        "port": 0,
        "query": "string",
        "rawAuthority": "string",
        "rawFragment": "string",
        "rawPath": "string",
        "rawQuery": "string",
        "rawSchemeSpecificPart": "string",
        "rawUserInfo": "string",
        "scheme": "string",
        "schemeSpecificPart": "string",
        "userInfo": "string"
      },
      "vcenterServerUuid": "string"
    }
  ],
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
			ds_type=dict(required=False, default='VVOL'),
			ds_name=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	ds_type = module.params['ds_type']
	ds_name = module.params['ds_name']

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

	vp = Datastore(
		port=port,
		url=host,
		token=token_id
	)

	res = vp.get_datastore(
		ds_type=ds_type,
		ds_name=ds_name
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
