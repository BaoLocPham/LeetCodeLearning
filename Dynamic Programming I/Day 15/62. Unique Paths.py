class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach 1: DP
        # Time O(m*n) ¯\_(ツ)_/¯
        # See the whiteboard of this question
        # Space O(n)
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            # exclude the last element in row
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        # return the first element in row
        return row[0]
