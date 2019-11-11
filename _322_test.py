import unittest
from _322_coin_change import Solution

class Test(unittest.TestCase):
    def test_cases(self):
        coins, amt = [1, 2, 5], 11
        self.assertEqual(Solution().coinChange(coins, amt), 3) # 5, 5, 1
        coins, amt = [2], 3
        self.assertEqual(Solution().coinChange(coins, amt), -1) # not possible
        
if __name__ == "__main__":
    print("Running: Testing.py ------")
    unittest.main()