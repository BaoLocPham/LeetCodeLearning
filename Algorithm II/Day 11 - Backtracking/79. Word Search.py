class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Approach 1: DFS Recursive Backtrack
        # Time O(m*n*dfs) -> O(m*n*4^len(word))
        # Space O(n) -> size ò
        R, C = len(board), len(board[0])
        # store the already visited path
        path = set()
        def dfs(r, c, i):
            # if we found all the chars in word
            if i==len(word):
                return True
            # if we goes out of bound
            # if char not
            if r<0 or r>=R or c<0 or c>=C or word[i] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            path.remove((r, c))
            return res
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False