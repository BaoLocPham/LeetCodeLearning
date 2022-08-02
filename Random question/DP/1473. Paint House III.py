class Solution:
    # https://leetcode.com/problems/paint-house-iii/solution/
    # Approach recursion
    # M: houses, N: neighbors, T: colors
    # TIme  O(M*T*N^2)
    # Space O(M*T*N)
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = [[[0]*21 for i in range(100)] for j in range(100)]
        max_cost = 1000001
        
        totalColor = len(cost[0])
        
        def findMinCost(houses, cost, targetCount, currIndex, neighborCount, prevHouseColor):
            if currIndex == len(houses):
                # if all houses are traversed, check if neighborCount is as expected or not
                return 0 if neighborCount == targetCount else max_cost
            if neighborCount > targetCount:
                # if the neighborCount is more than the threshold, we can't have target neighbor
                return max_cost
            
            # if we already calculated the answer 
            if memo[currIndex][neighborCount][prevHouseColor] != 0:
                return memo[currIndex][neighborCount][prevHouseColor];
            
            minCost = max_cost
            # if the house is already painted, update the value accordingly
            if houses[currIndex] != 0:
                newNeighborCount = neighborCount + (1 if houses[currIndex] != prevHouseColor else 0)
                minCost = findMinCost(houses, cost, targetCount, currIndex + 1, newNeighborCount, houses[currIndex])
            else:
                
                for color in range(1, totalColor+1):
                    newNeighborCount = neighborCount + (1 if color != prevHouseColor else 0)
                    currCost = cost[currIndex][color-1] + findMinCost(houses, cost, targetCount, currIndex + 1, newNeighborCount, color)
                    minCost = min(minCost, currCost)
            memo[currIndex][neighborCount][prevHouseColor] = minCost
            return minCost
        
        answer = findMinCost(houses, cost, target, 0, 0, 0)
        return -1 if answer == max_cost else answer