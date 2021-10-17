class Solution:
    # Approach 1: DP
    # Time O(n*m)
    # Space O(n*m)
    # This problem is just similar to Longest Common Subsequence
    # All you need is find LCS and then use the len1+len2-2*lcs
    def LCS(self, word1:str, word2:str)-> int:
        dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.LCS(word1, word2)
        return len(word1)+len(word2)-2*lcs