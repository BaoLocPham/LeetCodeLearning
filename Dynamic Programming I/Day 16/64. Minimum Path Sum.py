class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Approach 1: DP foward
        # Time O(n*m)
        # Space O(n*m)
        m, n = len(grid), len(grid[0])
        sumGrid = [[0] * (n) for _ in range(m)]
        # handle edge case
        sumGrid[0][0] = grid[0][0]
        # left col
        for i in range(1, m):
            sumGrid[i][0] = sumGrid[i - 1][0] + grid[i][0]
        # top row
        for j in range(1, n):
            sumGrid[0][j] = sumGrid[0][j - 1] + grid[0][j]
            # let's calculate the sumGrid
        for i in range(1, m):
            for j in range(1, n):
                sumGrid[i][j] = min(sumGrid[i - 1][j], sumGrid[i][j - 1]) + grid[i][j]
        # print(sumGrid)
        return sumGrid[-1][-1]

        # Approach 2: optimize space
        # Time O(n*m)
        # Space O(1) in-place modifying
        m, n = len(grid), len(grid[0])
        # Handle edge case
        # top row
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        # left col
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            # calculate
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]