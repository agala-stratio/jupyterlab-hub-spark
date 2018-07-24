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

import unittest
from spark import Spark

class MockRequest(object):
    def __init__(self, uri):
        self.uri = uri

class JupyterSparkUiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = Spark(base_url='http://privateagent:1234/user/fulano')

    def test_update_port(self):
        spark = self.spark
        spark.update_port('4040')

        assert spark.url == 'http://localhost:4040'
        assert spark.proxy_root == '/spark/4040'
        assert spark.proxy_url == 'http://privateagent:1234/user/fulano/spark/4040'

    def test_backend_url(self):
        spark = self.spark
        spark.update_port('4040')
        request = MockRequest('http://privateagent:1234/user/fulano/spark/4040/other/path')
        assert spark.backend_url(request) == 'http://localhost:4040/other/path'
