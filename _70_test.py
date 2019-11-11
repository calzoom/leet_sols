import unittest
from _70_climbing_stairs import Solution

class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().climbStairs(2), 2)
        self.assertEqual(Solution().climbStairs(3), 3)
        self.assertEqual(Solution().climbStairs(4), 5) # 1111, 121, 211, 112, 22
        self.assertEqual(Solution().climbStairs(0), 1)
        
if __name__ == "__main__":
    print("Running: Testing.py ------")
    unittest.main()