class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(n)
        rs = [[1]]
        for i in range(1, numRows):
            rs.append([1]*(i+1))
            for j in range(1, i):
                rs[i][j] = rs[i-1][j-1]+rs[i-1][j]
        return rs