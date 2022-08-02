class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach: Implementation
        # Time O(n*m)
        # Space O(1)
        row, col = 0, len(matrix[0])-1
        n, m = len(matrix), len(matrix[0])
        while row<n and col>=0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col]>target:
                col -= 1
            else:
                row += 1
        return False