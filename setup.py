from __future__ import absolute_import, division, print_function

import os
import sys
import platform
from setuptools import setup, find_packages

_this = os.path.abspath(os.path.dirname(__file__))

long_description = ''
with open(os.path.join(_this, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(os.path.join(_this, 'code_faster', 'version.py')) as f:
    exec(f.read(), version)

def get_install_requirements():
    contents = open(os.path.join(_this, 'requirements.txt')).read()
    return [
        req for req in contents.split('\n')
        if req != '' and not req.startswith('#')
    ]

des_string = \
"""
    A cross-platform command line utility for bootstrapping and running code with tests.
"""

setup(
    name='code_faster',
    version=version['__version__'],
    description=des_string,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    url='https://github.com/rahulsrma26/code_faster',
    author='Rahul Sharma',
    author_email='rahulsrma26@gmail.com',
    license='',
    packages=find_packages(),
    package_data={
        'code_faster': ['sample/**/*'],
    },
    # include_package_data=True,
    install_requires=get_install_requirements(),
    entry_points={
        'console_scripts': [
            'cfetch = code_faster.fetcher:main',
            'crun = code_faster.runner:main',
        ],
    }
)
