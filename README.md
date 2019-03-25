# SAP Ansible Modules for NetApp VASA Appliance

!! Started with refactoring !!
This repository contains classes and modules to manage the NetApp VASA Appliances of SAP Converged Cloud.

## Requirements

  * NetApp VASA Provider Version 7.2.1
  * Ansible Version 2.6.2
  * Python Version l2.7.15rc1

## API Documentation

REST API Documentation: `https://<url>:8143/api/rest/swagger-ui.html#/`

## Structure

```
.
└── ansible
    ├── module_utils
    │   └── storage
    │       └── netapp
    │           └── vasa
    └── modules
        └── storage
            └── netapp
```

### Classes

We decided to use classes because we reuse our code in other tools as well.
You will find the respective method in the same namespace like the API documentation.

Example:

"GET - 'datastore information' - datastore"
`Datastore -> modules_utils/storage/netapp/vasa/datastore.py`

"POST - 'enable/disable vp' - product-capabilities"
`Datastore -> modules_utils/storage/netapp/vasa/product_capability.py`

### Modules

These Ansible Modules containing:
  * Meta Data
  * Ansible Documentation
  * Function of Ansible and NetApp VASA Provider

### Playbooks

Each module has an documented playbook which can viewed by ansible-doc.

Example:

`ansible-doc -M module/storage/netapp/vasa_appliance_management_certificate_details.py`