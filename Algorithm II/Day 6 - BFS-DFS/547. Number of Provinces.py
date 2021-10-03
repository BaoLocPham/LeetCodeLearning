class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Approach 1: DFS Recursive
        # Time O(m*n)
        # Space O(?)
        visited = set()
        numberOfProvinces = 0

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        for start in range(len(isConnected)):
            if start not in visited:
                numberOfProvinces += 1
                dfs(start)

        return numberOfProvinces
        # Approach 2: DFS Iterative
        # Time O(m*n)
        # Space O(n) -> Size of the stack
        R, C = len(isConnected), len(isConnected[0]) # honestly, adjacency matrix R=C 🙂
        visited = set()
        numberOfProvinces = 0
        stack = []
        for start in range(R):
            if start not in visited:
                numberOfProvinces += 1
                stack.append(start)
                while stack:
                    i = stack.pop()
                    visited.add(i)
                    for end in range(C):
                        if isConnected[i][end] and end not in visited:
                            stack.append(end)
        return numberOfProvinces

