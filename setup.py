#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from imp import load_source

setup(
    name='saml2',
    version=load_source('', 'saml2/_version.py').__version__,
    description='A python interface to produce and consume Security '
                'Assertion Markup Language (SAML) v2.0 messages.'
                'Adopted from `python-saml` library.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    author='TeamRocket Developers',
    author_email='matt@lebrun.org',
    url='https://github.com/TeamRocketDevelopers/python-saml2',
    packages=find_packages('.'),
    install_requires=(
        # Extensions to the standard Python datetime module.
        # Provides ability to easily parse ISO 8601 formatted dates.
        'python-dateutil',

        # lxml is the most feature-rich and easy-to-use library for
        # processing XML and HTML in the Python language.
        'lxml',

        # Python bindings for the XML Security Library.
        'xmlsec'
    ),
    extras_require={
        'test': (
            # Test runner.
            'pytest',

            # Ensure PEP8 conformance.
            'pytest-pep8',

            # Ensure PyFlakes conformance.
            'pytest-flakes',

            # Ensure test coverage.
            'pytest-cov',
        )
    }
)
