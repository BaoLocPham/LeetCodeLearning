class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Approach 1: DP
        # Time O(m+n)
        # Space O(m+n)
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1,-1, -1):
                if text2[j]==text1[i]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]