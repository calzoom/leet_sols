import unittest
from _maxsubarraysum import Solution

class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().max_subarray_sum([-1, 2, 4, -3, 5, 2 ,-5, 2]), 10)
        
if __name__ == "__main__":
    print("Running: Testing.py ------")
    unittest.main()