# -*- coding: UTF-8 -*-
from distutils.core import setup

from setuptools import find_packages

from dodgy import __pkginfo__

_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "Searches for dodgy looking lines in Python code"

_install_requires = []

_classifiers = (
    'Development Status :: 7 - Inactive',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
)

setup(
    name='dodgy',
    url='https://github.com/landscapeio/dodgy',
    author='landscape.io',
    author_email='code@landscape.io',
    description=_short_description,
    install_requires=_install_requires,
    entry_points={
        'console_scripts': [
            'dodgy = dodgy.run:main',
        ],
    },
    version=__pkginfo__.get_version(),
    packages=_packages,
    license='MIT',
    keywords='check for suspicious code',
    classifiers=_classifiers
)
