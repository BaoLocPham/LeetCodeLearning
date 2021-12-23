class Solution:
    # Approach 1: DFS
    # Time O(n^n) TLE
    # Space O(?)
    def integerBreak(self, n: int) -> int:
        memoi = {}
        def dfs(num):
            if num==1:
                return 1
            if num not in memoi:
                rs = 0 if n==num else num
                for i in range(1,num):
                    val = dfs(i)*dfs(num-i)
                    rs = max(rs, val)
                memoi[num] = rs
            return memoi[num]
        return dfs(n)

    # Approach 2: DFS with memoization
    # Time O(n*m)
    # Space O(n)
    def integerBreak(self, n: int) -> int:
        memoi = {}
        def dfs(num):
            if num == 1:
                return 1
            if num not in memoi:
                rs = 0 if n == num else num
                for i in range(1, num):
                    val = dfs(i) * dfs(num - i)
                    rs = max(rs, val)
                memoi[num] = rs
            return memoi[num]
        return dfs(n)

    # Approach 3: DP
    # Time O(n*m)
    # Space O(n)
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        return dp[n]