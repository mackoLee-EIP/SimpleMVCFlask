from app import app
import json
import unittest

class SimpleControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass


    def test_query_test(self):
        params = {
            "a": "1"
        }
        res = self.app.get('/simple/test?a=1')

        self.assertDictEqual(params, res.get_json())

    def test_params_test(self):
        params = {
            "a": "1"
        }
        res = self.app.post('/simple/test', data=json.dumps(params), headers={"Content-Type": "application/json"})
        self.assertDictEqual(params, res.get_json())
