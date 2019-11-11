class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] := min number of coins needed to make amount i

        # for c in Coins: if amt - c > 0 take minimum across the options

        dp = [float("inf")] * (amount + 1)

        if amount < 0:
            return -1

        dp[0] = 0
        
        for i in range(len(dp)): # [0, amount]
            for c in coins:
                if (i - c) >= 0:
                    dp[i] = min(dp[i - c] + 1, dp[i]) # the min number of coins to make i is min of using every coin

        if dp[amount] == float("inf"):
            return -1

        else:
            return dp[amount]