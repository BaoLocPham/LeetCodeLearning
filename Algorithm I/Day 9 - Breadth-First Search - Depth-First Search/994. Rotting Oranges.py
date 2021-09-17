class Solution:
    def isValid(self, neighbor: tuple, R, C):
        if 0 <= neighbor[0] < R and 0 <= neighbor[1] < C:
            return True
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is basic BFS problem
        # Approach 1: BFS
        # Time O(n*m)
        # Space O(n*) -> space for queue
        R, C = len(grid), len(grid[0])
        queue = []
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        indx = [1, 0, -1, 0]
        indy = [0, 1, 0, -1]
        minutes = 0  # keep tracks of minutes
        while queue and fresh > 0:
            minutes += 1  # update minutes
            for i in range(len(queue)):  # # iterate all of the rotten in the same queue levels aka in the same minutes
                i, j = queue.pop(0)
                for t in range(4):
                    neighbor = i + indx[t], j + indy[t]
                    if self.isValid(neighbor, R, C) and grid[neighbor[0]][neighbor[1]] == 1:
                        grid[neighbor[0]][neighbor[1]] = 2
                        fresh -= 1
                        queue.append(neighbor)
        if fresh:
            return -1
        else:
            return minutes
