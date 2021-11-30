class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: DP
        # Time O(n)
        # Space O(1)
        maxProfit=0
        minPrice=prices[0]
        for price in prices:
            if price>minPrice:
                maxProfit = max(maxProfit, price-minPrice)
            else:
                minPrice = price
        return maxProfit

        # Approach 2: Kanade's algorithm (in case there are negative)
        # Time O(n)
        # Space O(1)
        maxSoFar, maxEnd = 0, 0
        for i in range(1, len(prices)):
            maxEnd += prices[i] - prices[i - 1]
            if maxEnd < 0: # when profit is negative reset it to zero
                maxEnd = 0
            maxSoFar = max(maxSoFar, maxEnd)
        return maxSoFar