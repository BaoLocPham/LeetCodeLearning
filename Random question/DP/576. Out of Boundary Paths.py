class Solution:
    # Approach: Recursion
    # Time O(4^n) TLE :)
    # Space O(4^n)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
            return a + b + c + d
        
        return solve(startRow, startColumn, maxMove) % 10e+8+7
        
    # Approach: Recursion with memoization 
    # Time O(N*M*K) N:row, M:col, K:move
    # Space O(N*M*K)
    def findPaths(self, m: int, n: int, maxMove: int, i: int, j: int) -> int:
        memo = [[[-1]*(maxMove+1) for i in range(n+1)] for j in range(m+1)]
        M = 10e+8+7
        
        def solve(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if N<=0:
                return 0
            if memo[i][j][N]!=-1:
                return memo[i][j][N]
            a = solve(i+1, j, N-1)%M
            b = solve(i-1, j, N-1)%M 
            c = solve(i, j+1, N-1)%M
            d = solve(i, j-1, N-1)%M
            memo[i][j][N] = int((a+b+c+d)%M)
            return memo[i][j][N]
        return solve(i, j, maxMove)