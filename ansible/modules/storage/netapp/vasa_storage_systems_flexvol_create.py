#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.storage_systems import StorageSystems
from pyvasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_storage_systems_flexvol_create

short_description: storage systems of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- create a flexvol based on storage capability profile

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

  vserver:
    description:
    - storage virtual machine (vserver)
    required: true

  scp:
    description:
    - name of storage capability profile
    required: true

  aggregate:
    description:
    - netapp storage aggregate
    required: true

  cluster_ip:
    description:
    - netapp cluster ip
    required: true

  size:
    description:
    - flex volume size in MB
    required: true
'''

EXAMPLES = '''
 - name: "create a flexvol based on storage capability profile"
   local_action:
     module: vasa_storage_systems_flexvol_create
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     vserver: "{{ vserver }}"
     scp: "{{ scp }}"
     aggregate: "{{ aggregate }}"
     cluster_ip: "{{ cluster_ip }}"
     size: "{{ size }}"
'''

RETURN = '''
{
  "clusterName": "string",
  "responseMessage": "string",
  "return_code": "int",
  "vServerName": "string",
  "volume": {
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
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vc_user=dict(required=True, type='str'),
			vc_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			vserver=dict(required=True, type='str'),
			scp=dict(required=True, type='str'),
			aggregate=dict(required=True, type='str'),
			cluster_ip=dict(required=True, type='str'),
			size=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	vserver = module.params['vserver']
	scp = module.params['scp']
	aggregate = module.params['aggregate']
	cluster_ip = module.params['cluster_ip']
	size = module.params['size']

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

	res = vp.create_flexvol_by_scp(
		vserver=vserver,
		scp=scp,
		aggr=aggregate,
		cluster_ip=cluster_ip,
		volume=volume,
		size=size
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
