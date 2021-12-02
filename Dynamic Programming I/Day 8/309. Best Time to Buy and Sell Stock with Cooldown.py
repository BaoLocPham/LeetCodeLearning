class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: DP
        # for me, this is the most confused dp problem so far.
        # you have to come up with an idea of three states :)
        # Time O(n)
        # Space O(1)
        n = len(prices)
        if n < 2:  # well, you can't buy and sell on the same day man.
            return 0
        stateA = [0] * n  # hold, can sell
        stateB = [0] * n  # just sell, only rest
        stateC = [0] * n  # rest, can buy
        stateA[0] = -prices[0]  # -> in first iteration -> 0
        stateB[0] = -math.inf
        stateC[0] = 0
        for i in range(1, n):
            stateA[i] = max(stateA[i - 1], stateC[i - 1] - prices[i])
            stateB[i] = stateA[i - 1] + prices[i]
            stateC[i] = max(stateB[i - 1], stateC[i - 1])

        # return max of state just sell and max of state rest ¯\_(ツ)_/¯
        return max(stateB[-1], stateC[n - 1])