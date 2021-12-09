class NumMatrix:
    # Approach 1: DP
    # Same as Matrix Block sum
    # Time O(n*m)
    # Space O(n*m)
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.sumRange = self.createSumRange()
        print(self.sumRange)
    def createSumRange(self):
        sumRange = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                sumRange[i+1][j+1] = sumRange[i][j+1] + sumRange[i+1][j] - sumRange[i][j] + self.matrix[i][j]
        return sumRange.copy()
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1, col1+1,row2+1,col2+1
        return self.sumRange[row2][col2] - self.sumRange[row2][col1-1] - self.sumRange[row1-1][col2] + self.sumRange[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)