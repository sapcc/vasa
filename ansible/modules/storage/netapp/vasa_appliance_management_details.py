#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from pyvasa.appliance_management import ApplianceManagement

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'supported_by': 'community',
    'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_appliance_management_details

short_description: managing netapp vasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description:
- list details of netapp unified vasa appliance

options:
  host:
    description:
    - The ip or name of the vasa unified appliance to manage.
    required: true

  username:
    description:
    - vasa appliance username for login.
    required: true

  password:
    description:
    - vasa appliance password for login.
    required: true

  port:
    description:
    - The port of the vasa unified appliance to manage.
    required: false
    default: '8143'
'''

EXAMPLES = '''
 - name: "list details of vasa appliance"
   local_action:
     module: vasa_appliance_management_details
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     port: "{{ appliance_port }}"
'''

RETURN = '''
{
  "applianceDetails": {
    "buildDate": "string",
    "linuxReleaseVersion": "string",
    "name": "string",
    "release": "string",
    "version": "string"
  },
  "responseMessage": "string",
  "return_code": "int"
}
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True, type='str'),
            username=dict(required=True, type='str'),
            password=dict(required=True, type='str', no_log='true'),
            port=dict(required=False, default='8143')
        ),
        supports_check_mode=True
    )

    host = module.params['host']
    port = module.params['port']
    username = module.params['username']
    password = module.params['password']

    result = dict(changed=False)

    vp = ApplianceManagement(port=port, url=host, vp_user=username, vp_password=password)
    res = vp.get_appliance_details()

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
