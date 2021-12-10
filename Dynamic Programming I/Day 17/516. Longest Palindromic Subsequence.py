class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Approach 1: DP
        # this approach is brilliant but how you can figure out the solution in the 45' interview?
        # Time O(n^2)
        # Space O(n^2)
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]