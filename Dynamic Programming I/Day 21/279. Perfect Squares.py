class Solution(object):
    # Approach 1: DFS TLE T.T
    # Approach is the same with the coin change problem
    # Time O(n^m)
    # Space O(?)
    def numSquares(self, n):
        rs = self.numSquaresHelper(n)
        return rs

    def numSquaresHelper(self, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        cc = -1
        for i in range(1, amount + 1):
            c = self.numSquaresHelper(amount - i ** 2)
            if c >= 0:
                cc = c if cc <= 0 else min(cc, c)
        return -1 if cc < 0 else cc + 1

    # Approach 2: DFS with memoi TLE T.T
    # Space O(n*m)
    # Space O(n*m)
    def numSquares(self, n):
        memoi = {}
        rs = self.numSquaresHelper(n, memoi)
        return rs

    def numSquaresHelper(self, amount, memoi):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        if amount not in memoi:
            cc = -1
            end = int((amount) ** (1 / 2) + 1)
            for i in range(1, end):
                c = self.numSquaresHelper(amount - i ** 2, memoi)
                if c >= 0:
                    cc = c if cc <= 0 else min(cc, c)
            memoi[amount] = -1 if cc < 0 else cc + 1
        return memoi[amount]

    # Approach 3: DP Bottom Up
    # Time O(n*n^1/2)
    # Space O(n)
    def numSquares(self, n):
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                squares = s * s
                if target - squares < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - squares])
        return dp[n]