class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: search from top right
        # Time O(m*n)
        # Space O(1)
        # Start searching from top right corner
        row, col = 0, len(matrix[0])-1
        while col>=0 and row<=(len(matrix)-1):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else: # matrix[row][col]<target:
                row+=1
        return False