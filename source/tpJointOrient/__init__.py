#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpJointOrient
"""

from __future__ import print_function, division, absolute_import

import os
import sys

from tpPyUtils import logger as logger_utils

# =================================================================================

logger = None

# =================================================================================


class tpJointOrient(object):
    def __init__(self):
        super(tpJointOrient, self).__init__()

    @classmethod
    def initialize(cls, do_reload=False):
        cls.create_logger()

        if do_reload:
            cls.reload_all()

    @staticmethod
    def create_logger():
        """
        Creates and initializes tpJointOrient logger
        """

        global logger
        logger = logger_utils.Logger(name=tpJointOrient.__name__, level=logger_utils.LoggerLevel.WARNING).logger
        logger.debug('Initializing tpJointOrient Logger ...')
        return logger

    @staticmethod
    def reload_all():
        # if os.environ.get('SOLSTICE_DEV_MODE', '0') == '1':
        import inspect
        scripts_dir = os.path.dirname(__file__)
        for key, module in sys.modules.items():
            try:
                module_path = inspect.getfile(module)
            except TypeError:
                continue
            if module_path == __file__:
                continue
            if module_path.startswith(scripts_dir):
                reload(module)


def run(do_reload=False):
    tpJointOrient.initialize(do_reload=do_reload)
    from tpJointOrient import jointorient
    win = jointorient.run()
    return win
