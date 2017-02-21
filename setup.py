#!/usr/bin/env python

from setuptools import setup

setup(
    name='sean',
    version='0.8.0.2',
    description=('Sean is a JSON structure factory.'),
    author='https://github.com/tuxxy/',
    author_email='me@johnpacific.com',
    url='https://github.com/tuxxy/Sean',
    install_requires=[
        'faker',
    ],
    packages=[
        'sean',
    ])
