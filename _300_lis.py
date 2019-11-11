class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0: # don't forget case when nums = []
            return 0

        # dp[i] = length of longest subsequence where the subarrays ends on element i
        
        dp  = [1] * len(nums) # solution to this will be max of this list

        for i in range(len(nums)): # i is ptr to element within nums we are prefixing to

            for j in range(i): # j is ptr to element within nums (j < i) 

                if nums[j] < nums[i]:

                    dp[i] = max(dp[j] + 1, dp[i]) # update whether or not this is maximized using this element

        return max(dp)