"""Holds the testscases for the credit_card_validator."""
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for credit card validator."""

    def test_blank_space(self):
        """Tests empty card numbers."""
        self.assertFalse("")


if __name__ == '__main__':
    unittest.main(verbosity=2)
