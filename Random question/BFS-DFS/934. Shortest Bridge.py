class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Using DFS and BFS
        # Time O(n^2)
        # Space O(n^2)
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]] # right, left, up, down
        
        def invalid(r, c):
            return r < 0 or c < 0 or r==N or c==N
        
        visited = set()
        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc, in direct:
                dfs(r + dr, c + dc)
                
        def bfs(r, c):
            res, queue = 0, deque(visited)
            while queue:
                length = len(queue)
                for i in range(length):
                    r, c = queue.popleft()
                    for dr, dc in direct:
                        curR, curC = r+dr, c+dc
                        if invalid(curR, curC) or (curR, curC) in visited:
                            continue
                        if grid[curR][curC]:
                            return res
                        visited.add((curR, curC))
                        queue.append((curR, curC))
                res +=1
            
                
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs(r, c)