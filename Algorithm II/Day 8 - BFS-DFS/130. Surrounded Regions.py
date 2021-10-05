class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Approach 1: DFS
        # Time O(n*m)
        # Space O(n)

        R, C = len(board), len(board[0])
        def captureT(r, c):
            if r < 0 or c < 0 or r == R or c == C or board[r][c] != "O":
                return
            board[r][c] = "T"
            captureT(r + 1, c)
            captureT(r - 1, c)
            captureT(r, c + 1)
            captureT(r, c - 1)

        # 1. Capture all unsurrounded regions -> DFS
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and r in [0, R - 1] or c in [0, C - 1]:
                    captureT(r, c)

        # 2. Capture all surrounded regions
        # 3. Upcapture all unsurrounded regions
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"