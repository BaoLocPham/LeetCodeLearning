class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Approach 1: Travel matrix
        # Time O(n*m) -> each cell is traveled once.
        # Space O(n+m)
        rowStart, rowEnd = 0, len(matrix)-1
        colStart, colEnd = 0, len(matrix[0])-1
        rs = []
        while rowStart<=rowEnd and colStart<=colEnd:
            # Travel right
            for i in range(colStart, colEnd+1):
                rs.append(matrix[rowStart][i])
            rowStart +=1
            # Travel down
            for i in range(rowStart, rowEnd+1):
                rs.append(matrix[i][colEnd])
            colEnd -=1
            # Travel left
            if (rowStart<=rowEnd):
                for i in range(colEnd, colStart-1, -1):
                    rs.append(matrix[rowEnd][i])
                rowEnd-=1
            # Travel up
            if (colStart<=colEnd):
                for i in range(rowEnd, rowStart-1, -1):
                    rs.append(matrix[i][colStart])
                colStart +=1
        return rs