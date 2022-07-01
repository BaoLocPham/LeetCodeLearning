class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Similar 1143. Longest Common Subsequence
        # Find LCS and the using the formular
        # m + n - 2*LCS
        # Time O(n*m)
        # Space O(n*m)
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return m + n - 2*dp[m][n]