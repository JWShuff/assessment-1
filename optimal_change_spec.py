import unittest
from optimal_change import optimal_change

class TestOptimalChange(unittest.TestCase):

    """
    When you call optimal_change you get a string back.
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
    def test_returns_proper_change1(self):
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_returns_proper_change2(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")


    """
    When you call optimal change with change due of .01, you get back 1 penny.
    """
    def test_handles_one_penny(self):
        self.assertEqual(optimal_change(.02, .03), "The optimal change for an item that costs $0.02 with an amount paid of $0.03 is 1 penny.")

    """
    When you call optimal change with change due of .04 you get back 4 pennies.
    """
    def test_handles_plural_pennies(self):
        self.assertEqual(optimal_change(.05, .09), "The optimal change for an item that costs $0.05 with an amount paid of $0.09 is 4 pennies.")
    """
    When you call optimal change with a change due of .05, you don't get back pennies.
    """
    def test_handles_small_change(self):
        self.assertFalse(optimal_change(.04, .09) == "The optimal change for an item that costs $0.04 with an amount paid of $0.09 is 5 pennies.")

    """
    When you call optimal change with large values, you get the proper result back.
    """
    def test_handles_large_values(self):
        self.assertEqual(optimal_change(1956.43, 3156.75), "The optimal change for an item that costs $1956.43 with an amount paid of $3156.75 is 12 $100 bills, 1 quarter, 1 nickel, and 2 pennies.")

    """
    Test returns correct full dollar amount of change.
    """
    def test_returns_four_dollars(self):
        self.assertEqual(optimal_change(6,10), "The optimal change for an item that costs $6 with an amount paid of $10 is 4 $1 bills.")
    """
    Test detects rounding issues at edge case conditions (.6 pennies more than cost.
    """
    def test_int_conversion_and_rounding(self):
        self.assertEqual(optimal_change(.1, .106), "You aren't paying with legal tender.")

if __name__ == '__main__':
    unittest.main()
    