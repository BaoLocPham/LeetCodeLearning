class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Approach 1: hashMap
        # Time O(n)
        # Space O(n)
        count = [0]*(n)
        for s, t in edges:
            count[t]+=1
        rs = []
        for i in range(n):
            if count[i]==0: rs.append(i)
        return rs