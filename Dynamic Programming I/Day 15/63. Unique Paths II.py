class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Approach 1: DP
        # Same approach as Unique Path I
        # Time O(n*m)
        # Space O(n*m)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [1]*(n)
        if obstacleGrid[-1][-1] == 1:
            return 0

        for i in range(n-2, -1, -1):
            row[i] = 1 if obstacleGrid[-1][i] != 1 and row[min(n-1, i+1)]!=0 else 0

        for i in range(m - 2, -1, -1):
            newRow = [0] * (n)
            newRow[-1] = 1 if obstacleGrid[i][-1] != 1 and row[-1] != 0 else 0

            # when start at n-1 -> all ways is just go straight down -> 1
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    newRow[j] = 0
                else:
                    newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # Approach 2: dp inplace modify
        # Time O(n*m)
        # Space O(1)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # check if the start and end is have an obstacle
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        # Number of ways at the end -> 1
        obstacleGrid[-1][-1] = 1

        # filling the last column of the grid:
        for i in range(m - 2, -1, -1):
            obstacleGrid[i][-1] = int(obstacleGrid[i][-1] == 0 and obstacleGrid[i + 1][-1] == 1)

        # filling the last row
        for i in range(n - 2, -1, -1):
            obstacleGrid[-1][i] = int(obstacleGrid[-1][i] == 0 and obstacleGrid[-1][i + 1] == 1)

        # Iterating from end point to start point
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    # rs = Right + Down
                    obstacleGrid[i][j] = obstacleGrid[i][j + 1] + obstacleGrid[i + 1][j]
        return obstacleGrid[0][0]