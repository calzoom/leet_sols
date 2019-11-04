import unittest
from _76_Minimum_Window_Substring import Solution

class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", "ZGB"), "")
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", ""), "")
        self.assertEqual(Solution().minWindow("JAPJOT", "JOT"), "JOT")
        self.assertEqual(Solution().minWindow("ENIGMA", "AN"), "NIGMA")
        self.assertEqual(Solution().minWindow("ENIGMA", "AEGIMN"), "ENIGMA")
        self.assertEqual(Solution().minWindow("", "ABC"), "")
        self.assertEqual(Solution().minWindow("", ""), "")
        self.assertEqual(Solution().minWindow("ab", "b"), "b")
        self.assertEqual(Solution().minWindow("abc", "c"), "c")
        
if __name__ == "__main__":
    print("Running: Testing.py ------")
    unittest.main()