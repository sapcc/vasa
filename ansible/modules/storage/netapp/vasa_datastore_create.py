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
module: vasa_datastore_create

short_description: datastore handle of netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- create a datastore container on vcenter

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

  cluster_ip:
    description:
    - cluster ip of netapp storage
    required: true

  ds_type:
    description:
    - type of the datastore
    required: false
    default: 'VVOL'

  scp:
    description:
    - name of the storage capability profile
    required: true

  description:
    description:
    - description of new datastore
    required: true

  flexvol:
    description:
    - mapped flexvolume(s)
    required: true

  ds_name:
    description:
    - name of the datastore
    required: true

  protocol:
    description:
    - protocol of storage (accepted values - ISCSI, NFS, VMFS)
    required: true

  target:
    description:
    - target moref
    required: true

  vserver:
    description:
    - name of the storage virtual machine (vserver)
    required: true
'''

EXAMPLES = '''
 - name: "create datastore on vcenter"
   local_action:
     module: vasa_datastore_create
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     cluster_ip: "{{ cluster_ip }}"
     ds_type: "{{ datastore_type }}"
     scp: "{{ scp }}"
     description: "{{ description }}"
     flexvol: "{{ flexvol }}"
     ds_name: "{{ datastore_name }}"
     protocol: "{{ protocol }}"
     target: "{{ target }}"
     vserver: "{{ vserver }}"
'''

RETURN = '''
{
  "responseMessage": "string",
  "return_code": "int",
  "taskID": 0
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vc_user=dict(required=True, type='str'),
			vc_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143'),
			cluster_ip=dict(required=True, type='str'),
			ds_type=dict(required=False, default='VVOL'),
			scp=dict(required=True, type='str'),
			description=dict(required=True, type='str'),
			flexvol=dict(required=True, type='str'),
			ds_name=dict(required=True, type='str'),
			protocol=dict(required=True, type='str'),
			target=dict(required=True, type='str'),
			vserver=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	cluster_ip = module.params['cluster_ip']
	ds_type = module.params['ds_type']
	scp = module.params['scp']
	description = module.params['description']
	flexvol = module.params['flexvol']
	ds_name = module.params['ds_name']
	protocol = module.params['protocol']
	target = module.params['target']
	vserver = module.params['vserver']

	result = dict(changed=False)

	connect = UserAuthentication(
		port=port,
		url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.login()
	token_id = token.get('vmwareApiSessionId')

	vp = Datastore(
		port=port,
		url=host,
		token=token_id
	)

	res = vp.create_datastore(
		cluster_ip=cluster_ip,
		ds_type=ds_type,
		scp=scp,
		description=description,
		flexvol=flexvol,
		ds_name=ds_name,
		protocol=protocol,
		target=target,
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
