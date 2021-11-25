class Solution:
    # Approach 1: Recursion TLE :(
    # Time O(2^n)
    # Space O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = min(self.minCost(cost, n-1), self.minCost(cost, n-2))
        return minCost
    def minCost(self, cost, index):
        if index<0: return 0
        if index==0 or index==1:
            return cost[index]
        else:
            return cost[index] + min(self.minCost(cost, index-1), self.minCost(cost, index-2))

    # Approach 2: Recursion but with memoization
    # Time O(n)
    # Space O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memoi = [0] * n
        minCost = min(self.minCost(cost, n - 1, memoi), self.minCost(cost, n - 2, memoi))
        return minCost

    def minCost(self, cost, index, memoi):
        if index < 0: return 0
        if index == 0 or index == 1:
            return cost[index]
        elif memoi[index] != 0:
            return memoi[index]
        else:
            memoi[index] = cost[index] + min(self.minCost(cost, index - 1, memoi), self.minCost(cost, index - 2, memoi))
            return memoi[index]

    # Approach 3: Bottom up with memoization
    # Time O(n)
    # Space O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memoi = [0] * n
        for i in range(n):
            if i < 2:
                memoi[i] = cost[i]
            else:
                memoi[i] = cost[i] + min(memoi[i - 1], memoi[i - 2])
        return min(memoi[n - 1], memoi[n - 2])

    # Approach 4: Bottom up optimized
    # Time O(n)
    # Space O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[0], cost[1]
        if n <= 2: return min(a, b)
        for i in range(2, n):
            tmp = cost[i] + min(a, b)
            a = b
            b = tmp
        return min(a, b)