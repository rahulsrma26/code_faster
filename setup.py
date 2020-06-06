from __future__ import absolute_import, division, print_function

import os
import sys
import platform
from setuptools import setup, find_packages

_this = os.path.abspath(os.path.dirname(__file__))

# version = {}
# with open(os.path.join(_this, 'src', 'code_faster', 'version.py')) as f:
#     exec(f.read(), version)


def get_install_requirements():
    contents = open(os.path.join(_this, 'requirements.txt')).read()
    return [
        req for req in contents.split('\n')
        if req != '' and not req.startswith('#')
    ]

setup(
    # version=version['__version__'],
    version='0.4.1',
    # package_data={
    #     'code_faster': ['sample/**/*'],
    # },
    install_requires=get_install_requirements(),
    extras_require={  # Optional
        'dev': [
            'check-manifest'
            'pytest',
            'coverage',
            'tox',
            # 'sphinx',
            # 'pallets-sphinx-themes',
            # 'sphinxcontrib-log-cabinet',
            # 'sphinx-issues',
        ]
    }
)
