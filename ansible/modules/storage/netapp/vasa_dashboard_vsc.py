# Author Hannes Ebelt <hannes.ebelt@sap.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.storage.netapp.vasa.dashboard import Dashboard
from ansible.module_utils.storage.netapp.vasa.vasa_connect import VasaConnection

__metaclass__ = type

ANSIBLE_METADATA = {
	'metadata_version': '1.0',
	'supported_by': 'community',
	'status': ['preview']
}

DOCUMENTATION = '''
module: vasa_dashboard_vsc

short_description: managing dashboard of netapp pyVasa unified appliance
author: Hannes Ebelt (hannes.ebelt@sap.com)

description: fetch data from vsc dashboard of the pyVasa appliance

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
 - name: "fetch data from vsc dashbaord of pyVasa appliance {{ inventory_hostname }}"
   local_action:
     module: vasa_dashboard_vsc
     host: "{{ inventory_hostname }}"
     vc_user: "{{ username }}"
     vc_password: "{{ password }}"
     port: "{{ appliance_port }}"
'''

RETURN = '''
{
  "data": {
    "datastoreCapacity": {
      "all": {
        "asc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ]
      },
      "nfs": {
        "asc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ]
      },
      "vmfs": {
        "asc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "freeCapacity": 0,
            "freePercentage": 0,
            "id": "string",
            "iops": 0,
            "latency": 0,
            "moref": "string",
            "name": "string",
            "subType": "string",
            "totalCapacity": 0,
            "type": "string",
            "usedCapacity": 0,
            "usedPercentage": 0
          }
        ]
      }
    },
    "datastoreFreeCapacity": 0,
    "datastoreIOPS": {
      "all": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      },
      "nfs": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      },
      "vmfs": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      }
    },
    "datastoreLatency": {
      "all": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      },
      "nfs": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      },
      "vmfs": {
        "asc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ],
        "count": 0,
        "desc": [
          {
            "metric": "string",
            "moref": "string",
            "name": "string",
            "subtype": "string",
            "type": "string",
            "unit": "string",
            "value": 0
          }
        ]
      }
    },
    "datastoreUsedCapacity": 0,
    "logicalUsedSpace": 0,
    "nextRefresh": 0,
    "percentageSpaceSaved": 0,
    "physicalUsedSpace": 0,
    "readIOPS": 0,
    "timeStamp": 0,
    "totalIOPS": 0,
    "totalSpaceSaved": 0,
    "vmCommittedCapacity": {
      "asc": [
        {
          "committedCapacity": 0,
          "host": "string",
          "hostMoRef": "string",
          "latency": 0,
          "moRefType": "string",
          "moRefValue": "string",
          "name": "string",
          "powerState": "string",
          "uptime": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "committedCapacity": 0,
          "host": "string",
          "hostMoRef": "string",
          "latency": 0,
          "moRefType": "string",
          "moRefValue": "string",
          "name": "string",
          "powerState": "string",
          "uptime": 0
        }
      ]
    },
    "vmIOPS": {
      "asc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ]
    },
    "vmLatency": {
      "asc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ]
    },
    "vmLogicalSize": {
      "asc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ]
    },
    "vmThroughput": {
      "asc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "metric": "string",
          "moref": "string",
          "name": "string",
          "subtype": "string",
          "type": "string",
          "unit": "string",
          "value": 0
        }
      ]
    },
    "vmUptime": {
      "asc": [
        {
          "committedCapacity": 0,
          "host": "string",
          "hostMoRef": "string",
          "latency": 0,
          "moRefType": "string",
          "moRefValue": "string",
          "name": "string",
          "powerState": "string",
          "uptime": 0
        }
      ],
      "count": 0,
      "desc": [
        {
          "committedCapacity": 0,
          "host": "string",
          "hostMoRef": "string",
          "latency": 0,
          "moRefType": "string",
          "moRefValue": "string",
          "name": "string",
          "powerState": "string",
          "uptime": 0
        }
      ]
    },
    "writeIOPS": 0
  },
  "responseMessage": "string",
  "return_code": "int"
}
'''


def main():
	module = AnsibleModule(
		argument_spec=dict(
			host=dict(required=True, type='str'),
			vcenter_user=dict(required=True, type='str'),
			vcenter_password=dict(required=True, type='str', no_log='true'),
			port=dict(required=False, default='8143')
		),
		supports_check_mode=True
	)

	host = module.params['host']
	port = module.params['port']
	vc_user = module.params['vcenter_user']
	vc_password = module.params['vcenter_password']

	result = dict(changed=False)

	connect = VasaConnection(
		port=port, url=host,
		vcenter_user=vc_user,
		vcenter_password=vc_password
	)

	token = connect.new_token()

	vp = Dashboard(
		port=port,
		url=host,
		token=token
	)

	res = vp.vsc_dashboard()

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
