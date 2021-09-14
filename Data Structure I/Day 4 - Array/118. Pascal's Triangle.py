class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Same as Reshape the matrix, this approach just straightforward
        # This tag as DP, but at this time i still don't know how to DP.
        # Keep learning !!!
        rs = [[1]]
        for i in range(1, numRows):
            rs.append([1]*(i+1))
            for j in range(1, i):
                rs[i][j] = rs[i-1][j-1]+rs[i-1][j]
        return rs