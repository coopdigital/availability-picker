import unittest
import app
import json

class ApiTests(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_availiability(self):
        sku = "123"
        r = self.app.get('/availability/{}'.format(sku))
        j = json.loads(r.data)
        self.assertTrue("sku" in j.keys())
        self.assertTrue("quantity" in j.keys())
        self.assertTrue(j['quantity'] > 0)
