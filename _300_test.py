import unittest
from _300_lis import Solution

class Test(unittest.TestCase):
    def test_cases(self):
        lst = [10,9,2,5,3,7,101,18]
        self.assertEqual(Solution().lengthOfLIS(lst), 4) # 2 3 7 101

        lst = [3, -1, 5, 4, -3, 100, 3, 8, 3]
        self.assertEqual(Solution().lengthOfLIS(lst), 3) # -3, 3, 8

        lst = [-1, -2, -3, -4, -5]
        self.assertEqual(Solution().lengthOfLIS(lst), 1) # 1
        
if __name__ == "__main__":
    print("Running: Testing.py ------")
    unittest.main()