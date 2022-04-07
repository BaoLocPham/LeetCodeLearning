class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Greedy
        # Time O(nlogn)
        # Space O(n)
        diffs = []
        for i in range(len(costs)):
            diffs.append([costs[i][1]-costs[i][0], costs[i][0], costs[i][1]])
        diffs.sort()
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs)//2:
                res += diffs[i][2] # get B
            else:
                res += diffs[i][1] # get A
        
        return res