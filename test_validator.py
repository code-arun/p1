import unittest
from  validato import *

class ValidatorTests(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(validator(''))

    def test_too_short(self):
        self.assertFalse(validator('aAbB1!?'))

    def test_too_long(self):
        self.assertFalse(validator('aA1!?' * 4 + 'a'))

    def test_no_number(self):
        self.assertFalse(validator("aAbBcC!?"))

    def test_no_upper(self):
        self.assertFalse(validator("aabbzz()"))

    def test_no_lower(self):
        self.assertFalse(validator("%&AABBCC"))

    def test_no_special(self):
        self.assertFalse(validator("aAbmMC19"))

    def test_valid(self):
        self.assertTrue(validator("a1?mzuF4"))


if __name__ == '__main__':
    unittest.main()
