class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # This problem is DFS
        R, C = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        # Approach 1: Recursion
        # def dfs(r, c) -> int:
        #     if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or grid[r][c] == 0:
        #         return 0
        #     visited.add((r, c))
        #     return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        #
        # for i in range(R):
        #     for j in range(C):
        #         if grid[i][j] and (i, j) not in visited:
        #             maxArea = max(maxArea, dfs(i, j))

        # Approach 2: Iteration
        for r0 in range(R):
            for c0 in range(C):
                if (r0, c0) not in visited and grid[r0][c0]:
                    shape = 0
                    stack = [(r0, c0)]
                    visited.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for rr, cc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] and (rr, cc) not in visited:
                                stack.append((rr, cc))
                                visited.add((rr, cc))
                    maxArea = max(maxArea, shape)
        return maxArea
