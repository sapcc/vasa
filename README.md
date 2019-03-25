# SAP Ansible Modules for NetApp VASA Appliance

This repository contains classes and modules to manage the NetApp VASA Appliances of SAP Converged Cloud.

## Requirements

  * NetApp VASA Provider Version 7.2.1
  * Ansible Version 2.6.2
  * Python Version l2.7.15rc1
  * pyVasa package

## API Documentation

REST API Documentation: `https://<url>:8143/api/rest/swagger-ui.html#/`

## Structure

```
.
└── ansible
    └── modules
        └── storage
            └── netapp
```

### pyVasa package

Use pip install to install pyVasa package.

### Modules

These Ansible Modules containing:
  * Meta Data
  * Ansible Documentation
  * Function of Ansible and NetApp VASA Provider

### Playbooks

Each module has an documented playbook which can viewed by ansible-doc.

Example:

`ansible-doc -M module/storage/netapp/vasa_appliance_management_certificate_details.py`