"""Holds the testscases for the credit_card_validator."""
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for credit card validator."""

    def test_empty(self):
        """Asserts empty card numbers should be invalid.
        Important for basic size category."""
        self.assertFalse(credit_card_validator(""))

    def test_one(self):
        """Asserts card numbers with length 1 should be invalid.
        Important for basic size category."""
        self.assertFalse(credit_card_validator("4"))

    def test_alpha_1(self):
        """Asserts a card number of length 16 with any alpha characters should
        be invalid. Important for symbol detection."""
        num = r"a!@#$%^&*( ()__+"
        self.assertFalse(credit_card_validator(num))

    def test_alpha_2(self):
        """Asserts a card number of length 15 with any alpha characters should
        be invalid. Important for symbol detection."""
        num = "==-=aaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test_alpha_3(self):
        """Asserts a card number of mixed nums with chars of len 16 should be
        invalid. Important for symbol detection."""
        num = "41a1aaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test_alpha_4(self):
        """Asserts a card number of mixed nums with chars of len 16 should be
        invalid. Important for symbol detection."""
        num = "41a1aaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test_random_prefix_1(self):
        """Tries to reject all numbers with length 16 and valid checksum
        but invalid prefixes. Important for finding bad prefixes."""
        num = num_with_checksum("123123123123123")
        self.assertFalse(credit_card_validator(num))

    def test_random_prefix_2(self):
        """Tries to reject all numbers with length 15 and valid checksum
        but invalid prefixes. Important for finding bad prefixes."""
        num = num_with_checksum("12312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_visa_length_big(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, and a length of 17 should be invalid.
        Important for length category."""
        num = num_with_checksum("4123123123123123")
        self.assertFalse(credit_card_validator(num))

    def test_visa_length_small(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, and a length of 15 should be invalid.
        Important for length category."""
        num = num_with_checksum("41231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_visa_checksum(self):
        """Asserts a visa card number with an invalid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be invalid.
        Important for checksum category."""
        num = "4123123123123129"
        self.assertFalse(credit_card_validator(num))

    def test_visa_bad_prefix_3(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, a prefix of 3 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("312312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_visa_bad_prefix_5(self):
        """Asserts a visa card number with an invalid checksum, non-alpha
        characters, a prefix of 5 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("512312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_visa_1(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be valid.
        Important for regular tests."""
        num = num_with_checksum("412312312312312")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_checksum_1(self):
        """Asserts a master card number with an invalid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be invalid.
        Important for checksum category."""

        num = "5312312312312319"
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_checksum_2(self):
        """Asserts a master card number with an invalid checksum, non-alpha
        characters, a prefix of 2225 and a length of 16 should be invalid.
        Important for checksum category."""

        num = "2225123123123129"
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_bad_prefix_50(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 50 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("501231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_bad_prefix_56(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 56 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("561231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_bad_prefix_2220(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 2220 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("222031231231231")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_bad_prefix_2721(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 2721 and a length of 16 should be invalid.
        Important for prefix category."""
        num = num_with_checksum("272131231231231")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_55(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 55 and a length of 16 should be valid.
        Important for regular tests."""
        num = num_with_checksum("551231231231231")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_2221(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 2221 and a length of 16 should be valid.
        Important for regular tests."""
        num = num_with_checksum("222112312312312")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_53(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be valid.
        Important for regular tests."""
        num = num_with_checksum("531231231231231")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_2225(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 2225 and a length of 16 should be valid.
        Important for regular tests."""
        num = num_with_checksum("222512312312312")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_53_length_big(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, and a length of 17 should be invalid.
        Important for size category."""
        num = num_with_checksum("5312312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_53_length_small(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, and a length of 15 should be invalid.
        Important for size category."""
        num = num_with_checksum("53123123123123")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_checksum_34(self):
        """Asserts an american express number with an invalid checksum,
        non-alpha characters, and a length of 15 should be invalid.
        Important for checksum category."""
        num = "341231231231239"
        self.assertFalse(credit_card_validator(num))

    def test_american_express_checksum_37(self):
        """Asserts an american express number with an invalid checksum,
        non-alpha characters, and a length of 15 should be invalid.
        Important for checksum category."""
        num = "371231231231239"
        self.assertFalse(credit_card_validator(num))

    def test_american_express_34(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 34 and a length of 15 should be valid.
        Important for checksum category."""
        num = num_with_checksum("34123123123123")
        self.assertTrue(credit_card_validator(num))

    def test_american_express_37(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 37 and a length of 15 should be valid.
        Important for regular testing."""
        num = num_with_checksum("37123123123123")
        self.assertTrue(credit_card_validator(num))

    def test_american_express_34_length_small(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 16 should be invalid.
        Important for size testing."""
        num = num_with_checksum("341231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_34_length_big(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 14 should be invalid.
        Important for size testing."""
        num = num_with_checksum("3412312312312")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_37_length_small(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 16 should be invalid.
        Important for size testing."""
        num = num_with_checksum("371231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_37_length_big(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 14 should be invalid.
        Important for size testing."""
        num = num_with_checksum("3712312312312")
        self.assertFalse(credit_card_validator(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
