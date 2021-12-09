class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # Approach 1: DP
        # Concept: https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
        # Time O(n*m)
        # Space O(n*m)
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rangeSum[i + 1][j + 1] = rangeSum[i][j + 1] + rangeSum[i + 1][j] - rangeSum[i][j] + mat[i][j]

        for i in range(m):
            for j in range(n):
                r1, r2, c1, c2 = max(0, i - k), min(m, i + k + 1), max(0, j - k), min(n, j + k + 1)
                dp[i][j] = rangeSum[r2][c2] - rangeSum[r2][c1] - rangeSum[r1][c2] + rangeSum[r1][c1]
        return dp