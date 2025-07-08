"""Holds the testscases for the credit_card_validator."""
import unittest
from credit_card_validator import credit_card_validator


# code adopted from wikipedia pseudocode of Luhn Algorithm
# https://en.wikipedia.org/wiki/Luhn_algorithm
def create_checksum(num):
    """Calculates the final checksum of a number as a string."""
    sum = 0
    i = len(num) - 1
    other_i = 0
    while True:
        if i < 0:
            break
        # selectively double characters depending on position
        n = 2 * int(num[i]) if other_i % 2 == 0 else int(num[i])
        # if doubling character results in > 9, subtract 9
        if n > 9:
            n -= 9
        # add number to working sum
        sum += n
        # update position and parity
        other_i += 1
        i -= 1
    return (10 - sum % 10) % 10


def num_with_checksum(num):
    """Creates a number with a checksum."""
    checksum = create_checksum(num)
    return num + str(checksum)


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for credit card validator."""

    def test_empty(self):
        """Asserts empty card numbers should be invalid."""
        self.assertFalse(credit_card_validator(""))

    def test_alpha_1(self):
        """Asserts a card number of length 16 with any alpha characters should
        be invalid."""
        num = "aaaaaaaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test_alpha_2(self):
        """Asserts a card number of length 15 with any alpha characters should
        be invalid."""
        num = "aaaaaaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def random_prefix_1(self):
        """Tries to reject all numbers with length 16 and valid checksum
        but invalid prefixes."""
        num = num_with_checksum("123123123123123")
        self.assertFalse(credit_card_validator(num))

    def random_prefix_2(self):
        """Tries to reject all numbers with length 15 and valid checksum
        but invalid prefixes."""
        num = num_with_checksum("12312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_visa_length_big(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, and a length of 17 should be invalid."""
        num = num_with_checksum("4123123123123123")
        self.assertFalse(credit_card_validator(num))

    def test_visa_length_small(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, and a length of 15 should be invalid."""
        num = num_with_checksum("41231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_visa_checksum(self):
        """Asserts a visa card number with an invalid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be invalid."""
        num = "412312312312312" + "9"
        self.assertFalse(credit_card_validator(num))

    def test_visa_1(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be valid."""
        num = num_with_checksum("412312312312312")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_checksum_1(self):
        """Asserts a master card number with an invalid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be invalid."""

        num = "531231231231231" + "9"
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_checksum_2(self):
        """Asserts a master card number with an invalid checksum, non-alpha
        characters, a prefix of 2225 and a length of 16 should be invalid."""

        num = "222512312312312" + "9"
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_1(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be valid."""
        num = num_with_checksum("531231231231231")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_2(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 2225 and a length of 16 should be valid."""
        num = num_with_checksum("222512312312312")
        self.assertTrue(credit_card_validator(num))

    def test_mastercard_length_big(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, and a length of 17 should be invalid."""
        num = num_with_checksum("5312312312312312")
        self.assertFalse(credit_card_validator(num))

    def test_mastercard_length_small(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, and a length of 15 should be invalid."""
        num = num_with_checksum("53123123123123")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_1(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 34 and a length of 15 should be valid."""
        num = num_with_checksum("34123123123123")
        self.assertTrue(credit_card_validator(num))

    def test_american_express_2(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 37 and a length of 15 should be valid."""
        num = num_with_checksum("37123123123123")
        self.assertTrue(credit_card_validator(num))

    def test_american_express_length_small(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 16 should be invalid."""
        num = num_with_checksum("341231231231231")
        self.assertFalse(credit_card_validator(num))

    def test_american_express_length_big(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, and a length of 14 should be invalid."""
        num = num_with_checksum("3412312312312")
        self.assertFalse(credit_card_validator(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
