class Solution:
    def average(self, salary: List[int]) -> float:
        # Time O(n)
        # Space O(1)
        n = len(salary)
        maxV, minV = float('-inf'), float('inf')
        summ = 0
        for s in salary:
            maxV = max(maxV, s)
            minV = min(minV, s)
            summ+=s
        return (summ-maxV-minV)/(n-2)