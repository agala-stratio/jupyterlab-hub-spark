#!/usr/bin/env python3
#
# © 2017 Stratio Big Data Inc., Sucursal en España. All rights reserved.
#
# This software – including all its source code – contains proprietary
# information of Stratio Big Data Inc., Sucursal en España and
# may not be revealed, sold, transferred, modified, distributed or
# otherwise made available, licensed or sublicensed to third parties;
# nor reverse engineered, disassembled or decompiled, without express
# written authorization from Stratio Big Data Inc., Sucursal en España.
#


import sys

from setuptools import find_packages, setup
import os

def setup_package():
    metadata = dict(
        name                = 'jupyter_spark_ui',
#    	packages            = ['jupyter_spark_ui'],
    	description         = """Jupyter Notebook extension to allow acces to the spark UI from the notebook server itself.""",
    	long_description    = "",
    	author              = "Stratio Intelligence",
    	platforms           = "Linux",
    	keywords            = [],
    	classifiers         = ['Programming Language :: Python :: 3'],
    )


    setup(**metadata)


if __name__ == '__main__':
    setup_package()
