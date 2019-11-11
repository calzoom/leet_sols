class Solution(object):
    def max_subarray_sum(self, lst):
        # for each array position, calculate the max subarray sum that ends on that position 

        # problem: find max subarray sum that ends at position k --> either singleton k, or subarray ending at k-1 and then include k
        """
        Key Insight:

        ---max_so_far--- --k-- ---future---

        k > k + max_so_far |====> k + future > k + max_sofar + future 
        """

        max_so_far, best = 0, 0
        for k in lst:
            max_so_far = max(k, max_so_far + k)
            best = max(best, max_so_far)

        return best
