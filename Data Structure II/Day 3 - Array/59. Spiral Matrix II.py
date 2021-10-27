class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Approach 1: Traverse Layer by Layer in Spiral Form
        # This problem is similar to the problem 54. Spinral Matrix 
        # Time O(n*m) -> Each cell is traveled once.
        # Space O(n*m)
        matrix = [[0]*n for i in range(n)]
        rowStart, rowEnd = 0, n-1
        colStart, colEnd = 0, n-1
        count = 1
        while rowStart<=rowEnd and colStart<=colEnd:
            # Travel right
            for i in range(colStart, colEnd+1):
                matrix[rowStart][i] = count
                count+=1
            rowStart +=1
            # Travel down
            for i in range(rowStart, rowEnd+1):
                matrix[i][colEnd] = count
                count+=1
            colEnd -=1
            # Travel left
            if (rowStart<=rowEnd):
                for i in range(colEnd, colStart-1, -1):
                    matrix[rowEnd][i] = count
                    count+=1
            rowEnd -=1
            # Travel up
            if (colStart<=colEnd):
                for i in range(rowEnd, rowStart-1, -1):
                    matrix[i][colStart] = count
                    count+=1
            colStart +=1
        return matrix