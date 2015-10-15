# -*- coding: utf-8 -*-
"""
Package-level constants and FdfError class
"""

"""
Created on Thu Jun 18 11:18:16 2015

@author: ktritz
"""
import os


FDF_DIR = os.path.dirname(os.path.abspath(__file__))
"""Path string: top-level directory for FDF package"""

MDS_SERVERS = {
    'nstx': 'skylark.pppl.gov:8501'
}
"""Dictionary: machine-name key paired to MDS server"""

LOGBOOK_CREDENTIALS = {
    'nstx': {
        'server': 'sql2008.pppl.gov\sql2008',
        'username': os.getenv('USER') or os.getenv('USERNAME'),
        'password': 'pfcworld',
        'database': 'nstxlogs',
        'port': '62917',
        'table': 'entries'
    }
}

_ALIASES = {
    'nstx': ['nstx', 'nstxu', 'nstx-u'],
}
"""Dictionary: machine-name key paired with logbook login credentials"""


def name(alias):
    global _ALIASES

    for key, value in iter(_ALIASES.items()):
        if alias.lower() in value:
            return key
    raise FdfError('{} not a valid machine name'.format(alias))


class FdfError(Exception):
    """
    Error class for FDF package

    **Usage**::

    raise FdfError('my error message')

    """
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message
