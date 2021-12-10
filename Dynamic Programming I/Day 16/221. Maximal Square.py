class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Approach 1: Brute Force
        # Time O((n*m)^2)
        # Space O(1) 
        m, n = len(matrix), len(matrix[0])
        maxLen = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    lenn = 1
                    flag = True
                    while (i + lenn < m and j + lenn < n and flag):
                        for k in range(j, lenn + j + 1):
                            if matrix[i + lenn][k] == "0":
                                flag = False
                                break
                        for k in range(i, lenn + i + 1):
                            if matrix[k][j + lenn] == "0":
                                flag = False
                                break
                        if flag:
                            lenn += 1
                    if maxLen < lenn:
                        maxLen = lenn
        return maxLen * maxLen

        # Approach 2: DP
        # using prefix sum array :V
        # Time O(n*m)
        # Space O(n*m)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxLen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen ** 2

        # Approach 3: Dp with better memory
        # same as approach 2 but only use 1D array instead of 2D
        # Time O(n*m)
        # Time O(n)
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        maxLen, prev = 0, 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    # prev -> dp[i-1][j-1]
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxLen ** 2
