import unittest
import sean
import json


class TestSeanExample(unittest.TestCase):
    def setUp():
        with open('example.sean') as f:            
            sean_data = f.read()
        self.sean_json = json.loads(sean_data)
        self.test_sean = sean.Sean(self.sean_json)
        self.exec_sean = self.test_sean.seanify()

    def test_sean_types(self):
        # Check there are SeanTypes in the expanded JSON
        is_correct = check_sean_types(self.test_sean.sean_types)
        self.assertTrue(is_correct)

    def test_execution(self):
        # Check there are no SeanTypes in the executed data
        is_correct = not check_sean_types(self.exec_sean)
        self.assertTrue(is_correct)


def check_sean_types(sean_data):
    is_correct = True
    for val in sean_data:
        if not isinstance(val, sean.seantype.SeanType):
            if isinstance(val, dict) or isinstance(val, list):
                self.test_sean_types(sean_data=val)
            else:
                is_correct = False
    return is_correct
