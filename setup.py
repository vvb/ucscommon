#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
    'nose'
]

setup(
    name='ucscommon',
    version='0.9.0.0',
    description="Common module that use the abstractions provided by other UCS Python SDKs",
    long_description=readme + '\n\n' + history,
    author="Cisco Ucs",
    author_email='ucs-python@cisco.com',
    url='https://github.com/ciscoucs/ucscommon',
    packages=[
        'ucscommon',
    ],
    package_dir={'ucscommon':
                 'ucscommon'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='ucscommon',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
