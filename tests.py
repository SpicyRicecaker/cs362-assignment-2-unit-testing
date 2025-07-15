"""Holds the testscases for the contrived_func."""
import unittest
import math
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    """Text fixture for the testcases for contrived_func."""

    def test_0(self):
        """Initial test case."""
        # Notation is in the form branch, conditions.
        # All coverable branches are covered.
        # Each condition state is unique, which is the
        # maximum possible for 8 tests.

        # TTT, TTFF
        contrived_func(2)
        # TTT, TTFT
        contrived_func(-1)
        # TFF, FTFF
        contrived_func(20)
        # TFF, TFFF
        contrived_func(3)
        # TFF, FTTF
        contrived_func(math.inf)
        # TFF, TFFT
        contrived_func(0)
        # FTF, FFTF
        contrived_func(93)
        # FFF, FFFF
        contrived_func(15)


if __name__ == '__main__':
    unittest.main()
