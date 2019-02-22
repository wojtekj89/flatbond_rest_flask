import unittest
import validators

class TestValidators(unittest.TestCase):

    def test_postcode(self):
        self.assertTrue(validators.validate_postcode('AA9A9AA')) 
        self.assertTrue(validators.validate_postcode('A9A9AA')) 
        self.assertTrue(validators.validate_postcode('W1A0AX')) 
        self.assertTrue(validators.validate_postcode('B338TH')) 
        self.assertFalse(validators.validate_postcode('invalid')) 
        self.assertFalse(validators.validate_postcode('AAAAAAA')) 


if __name__ == '__main__':
    unittest.main()