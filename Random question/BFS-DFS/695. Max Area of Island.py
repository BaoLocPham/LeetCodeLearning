class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach DFS
        # Time O(N*M)
        # Space O(N*M)
        R, C = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c]:
                    stack = [(r, c)]
                    visited.add((r, c))
                    shape = 0
                    while stack:
                        rr, cc = stack.pop()
                        shape+=1
                        for rrr, ccc in (rr+1, cc), (rr-1, cc), (rr, cc+1), (rr, cc-1):
                            if 0<=rrr<R and 0<=ccc<C and (rrr, ccc) not in visited and grid[rrr][ccc]:
                                stack.append((rrr, ccc))
                                visited.add((rrr, ccc))
                    maxArea = max(maxArea, shape)
        return maxArea
                        