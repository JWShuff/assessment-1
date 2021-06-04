import unittest

from optimal_change import optimal_change


class TestOptimalChange(unittest.TestCase):

    """
    When you call optimal_change you get a string back:
    """
    def test_returns_a_string(self):

        self.assertTrue(type(optimal_change(1, 1)) == type("string"))
    
    """
    When you call optimal_change with no change required you get back "No change due."
    """
    def test_returns_no_change(self):
        self.assertTrue(optimal_change(1, 1) == "No change due.")

    """
    When you call optimal change with cost > paid you get back "You have underpaid."
    """
    def test_returns_underpaid(self):
        self.assertTrue(optimal_change(4,1) == "You have underpaid.")

    """
    When you call optimal change, it properly returns the correct amount of change.
    """
    def test_returns_proper_change(self):
        self.assertTrue(optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

        self.assertTrue(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

if __name__ == '__main__':
    unittest.main()
