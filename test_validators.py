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

    def test_member_fee(self):
        minimum = 120 * 1.2 * 100 # 120 GBP + 20% VAT in pences
        self.assertTrue(validators.validate_fee(None, 100, minimum))
        self.assertFalse(validators.validate_fee({'fixed_membership_fee': True, 'fixed_membership_amount': 12000}, 50000, 12000))
        self.assertFalse(validators.validate_fee(None, 50000, minimum))
        self.assertTrue(validators.validate_fee({'fixed_membership_fee': False, 'fixed_membership_amount': 120}, 50000, 50000 * 1.2))

if __name__ == '__main__':
    unittest.main()