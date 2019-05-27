from setuptools import setup, find_packages

setup(
    name='pyVasa',
    version='0.1dev',
    description='Python package for NetApp VASA Appliance',
    license=open('LICENSE').read(),
    url='https://github.com/sapcc/vasa/pyVasa',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        'packaging==16.8',
        'requests==2.18.1',
        'urllib3==1.21.1'
        ]
    )
