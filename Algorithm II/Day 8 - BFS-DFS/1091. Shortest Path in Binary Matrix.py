from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Approach 1: BFS
        # Time O(m*n)
        # Space O(n) -> size of the queue
        queue = deque([(0, 0, 1)])
        visited = set()
        R, C = len(grid), len(grid[0])
        while queue:
            y, x, dist = queue.popleft()
            if (y, x) in visited or grid[y][x]==1:
                continue
            if (y, x) == (R-1, C-1):
                return dist
            visited.add((y, x))
            dx = [0, 0, 1, 1, 1, -1 , -1, -1]
            dy = [1, -1, 0, 1, -1, 0, 1, -1]
            for i in range(8):
                if 0<=x+dx[i]<C and 0<=y+dy[i]<R and grid[y+dy[i]][x+dx[i]]==0:
                    queue.append((y+dy[i], x+dx[i], dist+1))
        return -1

        # Approach 2: Optimized Code
        # Time O(m*n)
        # Space O(n) -> size of the queue
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n - 1 and j == n - 1: return d
            for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d + 1))
        return -1