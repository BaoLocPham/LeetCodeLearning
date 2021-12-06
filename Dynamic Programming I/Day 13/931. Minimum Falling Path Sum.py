class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(1) We inplace modify the matrix
        # key handle index outof bound max(0, j-1) and min(n-1, j+1)
        n = len(matrix)
        for i in range(1, n):
            for j in range(0, n):
                matrix[i][j] += min(matrix[i-1][max(0, j-1)], matrix[i-1][j], matrix[i-1][min(n-1, j+1)])
        return min(matrix[n-1])