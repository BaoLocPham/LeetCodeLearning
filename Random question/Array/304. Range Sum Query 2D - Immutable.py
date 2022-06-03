class NumMatrix:
    # Prefix sum theory
    # Time O(n*m) # creating the prefix sum
    # Space O(n*m) # storeing the prefix sum array
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixMat = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefixMat[r][c+1]
                self.prefixMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        
        bottomRight = self.prefixMat[r2][c2]
        above = self.prefixMat[r1-1][c2]
        left = self.prefixMat[r2][c1-1]
        topLeft = self.prefixMat[r1-1][c1-1]
        
        return bottomRight - left - above + topLeft
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)