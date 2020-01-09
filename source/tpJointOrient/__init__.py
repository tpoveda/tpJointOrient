#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpJointOrient
"""

from __future__ import print_function, division, absolute_import

import os
import inspect

from tpPyUtils import importer

# =================================================================================

logger = None

# =================================================================================


class tpJointOrient(importer.Importer, object):
    def __init__(self, *args, **kwargs):
        super(tpJointOrient, self).__init__(module_name='tpJointOrient', *args, **kwargs)

    def get_module_path(self):
        """
        Returns path where tpJointOrient module is stored
        :return: str
        """

        try:
            mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
        except Exception:
            try:
                mod_dir = os.path.dirname(__file__)
            except Exception:
                try:
                    import tpDccLib
                    mod_dir = tpDccLib.__path__[0]
                except Exception:
                    return None

        return mod_dir


def init(do_reload=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    """

    tpjointorient_importer = importer.init_importer(importer_class=tpJointOrient, do_reload=do_reload)

    global logger
    logger = tpjointorient_importer.logger

    tpjointorient_importer.import_modules()
    tpjointorient_importer.import_packages(only_packages=True)
    if do_reload:
        tpjointorient_importer.reload_all()


def run(do_reload=False):
    init(do_reload=do_reload)
    from tpJointOrient import jointorient
    win = jointorient.run()
    return win
