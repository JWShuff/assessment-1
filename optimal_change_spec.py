import unittest

from optimal_change import optimal_change


class TestOptimalChange(unittest.TestCase):

    """
    When you call optimal_change you get a string back:
    """

    def test_returns_a_string(self):

        self.assertTrue(type(optimal_change(1, 1)) == type("string"))
    """
    When you call optimal_change with no change required 
    """


if __name__ == '__main__':
    unittest.main()
