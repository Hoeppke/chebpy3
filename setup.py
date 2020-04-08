"""
Setup script for the chebpy3 project.
The chebpy3 project is a basic adaptation of the chebpy project to the new
python3 standard. It originates in a fork of the chebpy3 project.
"""
from distutils.core import setup

if __name__ == "__main__":
    params = {}
    params['name'] = 'chebpy3'
    params['version'] = '0.0.1dev'
    params['packages'] = ['chebpy3', 'chebpy3.core']
    params['license'] = 'MIT'
    setup(**params)
