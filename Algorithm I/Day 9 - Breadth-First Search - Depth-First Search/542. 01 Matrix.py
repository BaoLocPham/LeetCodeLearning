class Solution:
    def isValid(self, neighbor:tuple(), R, C):
        if 0 <= neighbor[0] < R and 0 <= neighbor[1] < C:
            return True
        return False

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Approach 1: BFS
        # Time O(r*c) -> Since, the new cells are added to the queue
        # only if their current distance is greater than the calculated distance,
        # cells are not likely to be added multiple times.
        # Space O(r*c) -> size of the queue
        R, C = len(mat), len(mat[0])
        dist = [[-1] * C for _ in range(R)]
        queue = []
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        indx = [1, 0, -1, 0]
        indy = [0, 1, 0, -1]
        while queue:
            i, j = queue.pop(0)
            for t in range(4):
                neighbor = i + indx[t], j + indy[t]
                if self.isValid(neighbor, R, C) and dist[neighbor[0]][neighbor[1]] == -1:
                    dist[neighbor[0]][neighbor[1]] = dist[i][j] + 1
                    queue.append(neighbor)
        return dist
        # Approach 2: Dynamic programming
        # Well, i still don't know how to DP.
        # Keep learing, this will be update in the future. XD