import unittest
from plates import is_valid

class TestLicensePlate(unittest.TestCase):

    def test_valid_plates(self):
        self.assertTrue(is_valid("CS50"))
        self.assertTrue(is_valid("ETO88"))

    def test_invalid_plates(self):
        self.assertFalse(is_valid("CS05"))
        self.assertFalse(is_valid("CS50P"))
        self.assertFalse(is_valid("PI3.14"))
        self.assertFalse(is_valid("H"))
        self.assertFalse(is_valid("OUTATIME"))
        self.assertFalse(is_valid("AA0"))
        self.assertFalse(is_valid("A.AB12"))
        self.assertFalse(is_valid("AA-123"))

if __name__ == '__main__':
    unittest.main()
