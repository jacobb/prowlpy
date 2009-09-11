#/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import sys

sys.path.append('python')

from prowlpy import __author__ 
from prowlpy import __version__

long_description = '''
Python module for posting to the iPhone Push Notification service Prowl: http://prowl.weks.net/
'''

setup(
        name = 'prowlpy',
        packages = ['prowlpy'],
        package_dir= {'prowlpy': 'python'},
        version = __version__,
        description= 'Python module for Prowl iPhone notification service',
        author = __author__,
)        
