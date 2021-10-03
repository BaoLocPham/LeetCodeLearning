class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1: DFS - Recursion
        # Time O(m*n)
        # Space O(?)
        dx = [0, -1, 1, 0]
        dy = [1, 0, 0, -1]
        R, C = len(grid), len(grid[0])
        numberOfIslands = 0

        def dfs(r, c):
            grid[r][c] = "-1"
            for k in range(4):
                rr, cc = r + dx[k], c + dy[k]
                if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == "1":
                    dfs(rr, cc)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numberOfIslands += 1
        return numberOfIslands

        # Approach 2: DFS - Iterative
        # Time O(m*n)
        # Space O(n) -> size of the stack
        R, C = len(grid), len(grid[0])
        stack = []
        dx = [0, -1, 1, 0]
        dy = [1, 0, 0, -1]
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    stack.append((i, j))
                    count += 1
                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = "-1"
                        for k in range(4):
                            rr, cc = r + dx[k], c + dy[k]
                            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == "1":
                                stack.append((rr, cc))
        return count