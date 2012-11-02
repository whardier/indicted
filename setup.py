#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

from indicted import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='indicted',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['indicted'],
    url='https://github.com/whardier/indicted',
    license='MIT',
    description='Indexed Dictionary Class',
    long_description=read('README'),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
)


