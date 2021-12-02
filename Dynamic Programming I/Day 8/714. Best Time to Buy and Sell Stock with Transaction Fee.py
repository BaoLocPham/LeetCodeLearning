class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach 1: DP
        # using two state to store maximum profit 
        # Time O(n)
        # Space O(1)
        # cash: maximum profit if we did not have a share of stock
        # hold: maximum profit if we did have a share of stock
        cash, hold = 0, -prices[0]
        # at the first iteration
        # cash = 0 #
        # hold = -prices[0] # because we don't have any profit yet
        for i in range(1, len(prices)):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash