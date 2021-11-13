class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Approach 1: hashMap
        # Time O(n)
        # Space O(n)
        count = [0]*(n+1)
        for s,t in trust:
            count[s]-=1
            count[t]+=1
        for i in range(1, n+1):
            if count[i]==n-1:
                return i
        return -1