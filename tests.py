"""Holds the testscases for the contrived_func."""
import unittest
import math
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for contrived_func."""

    def test_0(self):
        """Initial test case."""
        for val in [2, -1, 20, 3, math.inf, 666, 93, 15]:
            contrived_func(val)


if __name__ == '__main__':
    unittest.main()
