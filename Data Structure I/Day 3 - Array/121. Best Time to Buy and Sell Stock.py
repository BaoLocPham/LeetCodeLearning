class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This approach is whatever IDK :) somes said this is DP, somes didn't
        # Time O(n)
        # Space O(1) two variables are used
        maxProfitt = 0
        minPrice = prices[0]
        for i in prices:
            if minPrice>i:
                minPrice = i
            if maxProfitt<i-minPrice:
                maxProfitt = i-minPrice
        return maxProfitt