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

    def test1(self):
        """Asserts empty card numbers should be invalid."""
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, and a length of 17 should be invalid."""
        num = num_with_checksum("4123123123123123")
        self.assertFalse(credit_card_validator(num))

    def test3(self):
        """Asserts a card number of length 16 with any alpha characters should
        be invalid."""
        num = "aaaaaaaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test4(self):
        """Asserts a card number of length 15 with any alpha characters should
        be invalid."""
        num = "aaaaaaaaaaaaaaa"
        self.assertFalse(credit_card_validator(num))

    def test5(self):
        """Asserts a visa card number with an invalid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be invalid."""
        num = "412312312312319"
        self.assertFalse(credit_card_validator(num))

    def test6(self):
        """Asserts a visa card number with a valid checksum, non-alpha
        characters, a prefix of 4 and a length of 16 should be valid."""
        num = num_with_checksum("412312312312312")
        self.assertTrue(credit_card_validator(num))

    def test7(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be valid."""
        num = num_with_checksum("531231231231231")
        self.assertTrue(credit_card_validator(num))

    def test8(self):
        """Asserts a mastercard number with a valid checksum, non-alpha
        characters, a prefix of 53 and a length of 16 should be valid."""
        num = num_with_checksum("222512312312312")
        self.assertTrue(credit_card_validator(num))

    def test9(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 34 and a length of 15 should be valid."""
        num = num_with_checksum("34123123123123")
        self.assertTrue(credit_card_validator(num))

    def test10(self):
        """Asserts an american express number with a valid checksum, non-alpha
        characters, a prefix of 37 and a length of 15 should be valid."""
        num = num_with_checksum("37123123123123")
        self.assertTrue(credit_card_validator(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
