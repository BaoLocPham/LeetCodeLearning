class Solution:
    # Approach 1: Brute Force DFS
    # Time O(n^m)
    # Space O(?)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        elif amount<0:
            return -1
        cc = -1
        for coin in coins:
            c = self.coinChange(coins, amount-coin)
            if c>=0:
                cc = c if cc<0 else min(cc, c)
        return -1 if cc<0 else cc+1

    # Approach 2: Brute Force DFS with memoization
    # Time O(n*m)
    # Space O(n*m)
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoi = {}
        rs = self.coinChangeHelper(coins, amount, memoi)
        return rs

    def coinChangeHelper(self, coins, amount, memoi):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        if amount not in memoi:
            cc = -1
            for coin in coins:
                c = self.coinChangeHelper(coins, amount - coin, memoi)
                if c >= 0:
                    cc = c if cc < 0 else min(cc, c)
            memoi[amount] = -1 if cc < 0 else cc + 1
        return memoi[amount]

    # Approach 3: DP Bottom up
    # Time O(n*m)
    # Space O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(0, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] <= amount else -1