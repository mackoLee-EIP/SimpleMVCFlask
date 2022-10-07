from app import app
import unittest

class SimpleControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_test(self):
        print(1)
        print(self.app.get('/'))
