"""Holds the testscases for the credit_card_validator."""
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for credit card validator."""

    def test1(self):
        """Test testing function."""
        self.assertFalse(credit_card_validator(2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
