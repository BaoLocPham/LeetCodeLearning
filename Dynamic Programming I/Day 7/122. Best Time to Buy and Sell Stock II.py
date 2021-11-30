class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: DP
        # Seriously, there're more complex approach but why?
        # Time O(n)
        # Space O(1)
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit