class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach 1: Rotate Groups of Four Cells
        # Time O(n*m) -> each cell is getting read and written once.
        # Space O(1)
        n = len(matrix[0])
        for i in range(n//2+n%2):
            for j in range(n//2):
                tmp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-j-1]
                matrix[n-1-i][n-j-1] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp

        # Approach 2: using combination of transpose and reverse array
        # Time O(n*m) -> each cell is transpose and reverse once.
        # Space O(1)
        self.transpose(matrix)
        self.reverse(matrix)
        
    def transpose(self, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]