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
module: vasa_datastore_delete

short_description: datastore handle of netapp pyvasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- delete a datastore container on vcenter

options:
  host:
    description:
    - The ip or name of the pyvasa unified appliance to manage.
    required: true

  port:
    description:
    - The port of the pyvasa unified appliance to manage.
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

  ds_name:
    description:
    - name of the datastore
    required: true

  ds_type:
    description:
    - type of the datastore
    required: true
'''

EXAMPLES = '''
 - name: "delete datastore on vcenter"
   local_action:
     module: vasa_datastore_delete
     host: "{{ inventory_hostname }}"
     port: "{{ appliance_port }}"
     vc_user: "{{ vcenter_username }}"
     vc_password: "{{ vcenter_password }}"
     ds_name: "{{ datastore_name }}"
     ds_type: "{{ datastore_type }}"
'''

RETURN = '''
{
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
			ds_name=dict(required=True, type='str'),
			ds_type=dict(required=True, type='str')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vc_user']
	vc_password = module.params['vc_password']
	ds_name = module.params['ds_name']
	ds_type = module.params['ds_type']

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

	res = vp.datastore_delete(
		ds_moref=ds_name,
		ds_type=ds_type
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
