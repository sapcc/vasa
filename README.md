# SAP Ansible Modules and Python Package for NetApp VASA Appliance

This repository contains classes and modules to manage the NetApp VASA Appliances of SAP Converged Cloud.

## Requirements

  * NetApp VASA Provider Version 7.2.1
  * Ansible Version 2.7.15.rc1
  * Python Version 3.6.7
  * pyvasa package

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

### pyvasa package

Use pip install to install pyvasa package.

### Modules

These Ansible Modules containing:
  * Meta Data
  * Ansible Documentation
  * Function of Ansible and NetApp VASA Provider

### Playbooks

Each module has an documented playbook which can viewed by ansible-doc.

Example:

`ansible-doc -M module/storage/netapp/vasa_appliance_management_certificate_details.py`
