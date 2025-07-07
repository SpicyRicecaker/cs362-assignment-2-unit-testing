import unittest

def add_two(x):
    return x + 3

class TestCase(unittest.TestCase):
    def test_add_five(self):
        x = 5
        self.assertEqual(add_two(x), x + 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)