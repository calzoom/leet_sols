class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        dp = [0] * (n+1) # dp[i] := number of distinct ways to climb up i total steps

        # dp[1] = 1, dp[2] = 2 (11 2), dp[3] = 3 (111, 12, 21) 

        # dp[i] = dp[i - 1] + dp[i  - 2] 
        # to get to step i you could have either taken 1 step from i-1 or taken a 2 step from i-2, there's no other way (we don't look at taking 2 1-steps from i-2 because 1 of the 1-step puts you at i-1 and then you would be overcounting)
        # this is also just the nth fib number
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):   # O(n)
            ways = 0
            if dp[i - 1] > 0:
                ways += dp[i-1]
            if dp[i - 2] > 0:
                ways += dp[i-2]
            dp[i] += ways

        return dp[n]