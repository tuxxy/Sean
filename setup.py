#!/usr/bin/env python

from distutils.core import setup

setup(
    name='sean',
    version='0.8',
    description=('Sean is a JSON factory that produces events based on a',
        'certain schema'),
    author='https://github.com/tuxxy/',
    author_email='me@johnpacific.com',
    packages=[
        'sean',
        'sean.seantype',
        'sean.handlers'
    ])
