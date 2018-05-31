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
    """
    vasa provider
    """
    name = None
    status = None
    cluster = None
    role = None
    tenant = None
    platform = None
    ip4 = None
    ip6 = None
    vcpus = None
    memory = None
    disk = None
    comments = None
    customfields = None

    def __init__(self, platform='16', status='1', role='22', tenant='1', cluster='239', **kwargs):
        self.__dict__.update(kwargs)

        self.platform = platform
        self.status = status
        self.role = role
        self.tenant = tenant
        self.cluster = cluster
        self.ip4 = self.get_ipam_ipaddress()

    def create_vp(self):
        try:
            nb.virtualization.virtual_machines.create(
                name=self.name,
                status=self.status,
                cluster=self.cluster,
                role=self.role,
                tenant=self.tenant,
                platform=self.platform,
                primary_ip4=self.ip4,
                #primary_ip6=self.ip6,
                #vcpus=self.vcpus,
                #memory=self.memory,
                #disk=self.disk,
                #comments=self.comments,
                #custom_fields=self.customfields
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

    def get_virtualization_vm(self):
        vips = nb.ipam.ip_addresses.filter('vasa')
        result = []

        for vip in vips:
            r = dict()

            r['address'] = vip.address
            r['id'] = vip.id
            r['description'] = vip.description
            r['status'] = vip.status
            r['tenant'] = vip.tenant

            result.append(r)

        return result

    def get_ipam_ipaddress(self):
        #need ip_id for vp
        pass

    def get_virtualization_cluster(self):
        #need cluster_id for vp
        pass


ip4 = '8409'
name = 'vasa-bb110.cc.ap-ae-1.cloud.sap'

vasa = VasaProvider(ip4=ip4, name=name)

vasa.create_vp()
#vasa.get_vp()
