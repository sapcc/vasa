#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from pyvasa.datastore import Datastore
from pyvasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_datastore_scp_aggregates_filter

short_description: datastore handle of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- get list of provisioning capable aggregates available, satisfying requirement of given SCP(s) and protocol

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

  cluster:
    description:
    - storage cluster
    required: true

  vserver:
    description:
    - storage virtual machine name (vserver)
    required: true

  scp:
    description:
    - storage capability profile name
    required: true
'''

EXAMPLES = '''
 - name: "get list of provisioning capable aggregates available, satisfying requirement of given SCP(s) and protocol"
   local_action:
     module: vasa_datastore_scp_aggregates_filter
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     cluster: "{{ cluster }}"
     vserver-name: "{{ vserver }}"
     scp: "{{ scp }}"
'''

RETURN = '''
{
  "provisionableTargetAggregatesForSCP": [
    {
      "provisionableTargetAggregates": [
        {
          "maxVolumeSize": 0,
          "name": "string",
          "sizeAvailable": 0,
          "sizeTotal": 0,
          "sizeUsed": 0,
          "uuid": "string"
        }
      ],
      "scpName": "string"
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
			cluster=dict(required=True, type='str'),
			vserver=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	cluster = module.params['cluster']
	vserver = module.params['vserver']
	scp = module.params['scp']

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

	res = vp.datastore_aggregates_filter(
		scp=scp,
		cluster=cluster,
		vserver=vserver
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
