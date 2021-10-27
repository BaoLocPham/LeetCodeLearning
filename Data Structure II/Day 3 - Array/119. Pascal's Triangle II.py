class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Approach 1: Brute Force
        # Time O(n*m)
        # Spacce O(n*m)
        rs = [[1]]
        for r in range(1, rowIndex + 1):
            rs.append([1] * (r + 1))
            for c in range(1, r):
                rs[r][c] = rs[r - 1][c - 1] + rs[r - 1][c]
        return rs[rowIndex]
