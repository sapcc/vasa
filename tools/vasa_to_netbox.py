#author: Hannes Ebelt (hannes.ebelt@sap.com)

import ssl, pynetbox, requests, os, urllib3, datetime
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.environ["CURL_CA_BUNDLE"] = ""

try:
    '''
    netbox connection
    '''
    nb = pynetbox.api(
        'https://netbox.global.cloud.sap',
        token='6e25338eea833ecddf28dbc554a57e8e7955c99c'
    )
except pynetbox.RequestError as e:
    print(e.error)
    sys.exit(1)


class VasaProvider:
    def __init__(self, platform='16', status='1', role='22', tenant='1', **kwargs):
        self.__dict__.update(kwargs)

        self.platform = platform
        self.status = status
        self.role = role
        self.tenant = tenant

    def create_vp(self):
        try:
            nb.virtualization.virtual_machine.create(
                name=self.name,
                status=self.status,
                cluster=self.cluster,
                role=self.role,
                tenant=self.tenant,
                platform=self.platform,
                primary_ip4=self.ip4,
                primary_ip6=self.ip6,
                vcpus=self.vcpus,
                memory=self.memory,
                disk=self.disk,
                comments=self.comments,
                custom_fields=self.customfields
            )
        except pynetbox.RequestError as e:
            print(e.error)

    def update_vp(self):
        try:
            nb.virtualization.virtual_machine.save(
                name=self.name,
                status=self.status,
                cluster=self.cluster,
                role=self.role,
                tenant=self.tenant,
                platform=self.platform,
                primary_ip4=self.ip4,
                primary_ip6=self.ip6,
                vcpus=self.vcpus,
                memory=self.memory,
                disk=self.disk,
                comments=self.comments,
                custom_fields=self.customfields
            )
        except pynetbox.RequestError as e:
            print(e.error)

    def delete_vp(self):
        try:
            nb.virtualization.virtual_machine.delete(id=self.id_vm)
        except pynetbox.RequestError as e:
            print(e.error)

    def get_vp(self):
        vips = nb.ipam.ip_addresses.filter('vasa')
        result = []

        for vip in vips:
            r = {}
            r['address'] = vip.address
            r['id'] = vip.id
            r['description'] = vip.description
            r['status'] = vip.status
            r['tenant'] = vip.tenant

            result.append(r)

        return result


ip4 = '10.46.76.99'
name = 'vasa-bb110.cc.ap-ae-1.cloud.sap'

vasa = VasaProvider()

for i in vasa.get_vp():
    print(i)
