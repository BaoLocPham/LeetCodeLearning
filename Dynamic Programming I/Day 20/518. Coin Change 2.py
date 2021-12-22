class Solution:
    def change(self, amount, coins):
        # Approach 1: 2D DP
        # Time O(n*m)
        # Space O(n*m)
        coinLen = len(coins)
        dp = [[0]*(amount+1) for _ in range(coinLen+1)]
        dp[0][0] = 1
        # dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
        for i in range(1, coinLen+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                more = dp[i][j - coins[i-1]] if j>=coins[i-1] else 0
                dp[i][j] = dp[i-1][j] + more
        return dp[coinLen][amount]

        # ->> see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]],
        # then we can optimize the space by only using one-dimension array.

        # Approach 2: 1D DP space optimized
        # Time O(n*m)
        # Space O(n)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]