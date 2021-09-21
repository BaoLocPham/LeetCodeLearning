class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # This is a DP problem
        # Approach 1: Solving bottom up
        # Time O(n^2)
        # Space O(n) -> size of the memo
        dp = [0]*(len(triangle)+1)
        # we will solve this problem bottom up
        for i in range(len(triangle), -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
        return dp[0]