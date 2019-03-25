#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyVasa.datastore import Datastore
from pyVasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_datastore_scp_cluster_filter

short_description: datastore handle of netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- get list of clusters available, satisfying requirement of given SCP(s) and protocol

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

  scp:
    description:
    - storage capability profile name
    required: true

  protocol:
    description:
    - protocol of storage (accepted values - ISCSI, NFS, VMFS)
    required: true
'''

EXAMPLES = '''
 - name: "get list of clusters available, satisfying requirement of given SCP(s) and protocol"
   local_action:
     module: vasa_datastore_scp_cluster_filter
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     scp: "{{ scp }}"
     protocol: "{{ protocol }}"
'''

RETURN = '''
{
  "clusterList": [
    {
      "controllerIp": "string",
      "name": "string",
      "uuid": "string",
      "vserverReasons": [
        "string"
      ],
      "vservers": [
        {
          "aggregateNames": [
            "string"
          ],
          "availableSpace": 0,
          "controllerIp": "string",
          "controllerUsername": "string",
          "controllerUuid": "string",
          "failedReason": "string",
          "fcpEnabled": true,
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
          "id": "string",
          "iscsiEnabled": true,
          "name": "string",
          "ndmpAllowed": true,
          "nfs3Enabled": true,
          "nfs41Enabled": true,
          "nfsEnabled": true,
          "protocolEndpoints": [
            {
              "flexVolName": "string",
              "id": "string",
              "ipAddress": "string",
              "path": "string",
              "san": true,
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
      ]
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
			scp=dict(required=True, type='str'),
			protocol=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	scp = module.params['scp']
	protocol = module.params['protocol']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = Datastore(
		port=port,
		url=host,
		token=token
	)

	res = vp.datastore_cluster_filter(
		scp=scp,
		protocol=protocol
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
