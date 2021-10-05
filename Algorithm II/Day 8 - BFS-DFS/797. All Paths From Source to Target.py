class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Approach 1: DFS Recursive
        # Time O(2^n) -> travel fully connected acyclic graph -> O(2^n)
        # Space O(n)
        res = []
        path = []
        path.append(0)
        lastNode = len(graph) - 1
        def dfs(node):
            if node == lastNode:
                res.append(path.copy())
                return None
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(node=nextNode)
                # Pop the last node
                path.pop()
        dfs(0)
        return res

        # Approach 2: DFS Iterative
        # Time O(2^n)
        # Space O(n)
        res = []
        lastNode = len(graph) - 1
        # Store the first node and the path from that node
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == lastNode:
                res.append(path)
            for nextNode in graph[node]:
                # print(nextNode)
                stack.append((nextNode, path + [nextNode]))
        return res