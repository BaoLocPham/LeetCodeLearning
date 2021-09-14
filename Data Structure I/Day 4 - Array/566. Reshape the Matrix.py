class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # This approach is just straightforward
        rs = [[0] * c for _ in range(r)]
        if len(mat) * len(mat[0]) != r * c:
            return mat

        # oneD = [0]*(r*c)
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         oneD[len(mat[0])*i+j] = mat[i][j]
        # for i in range(len(oneD)):
        #     rs[i//c][i%c] = oneD[i]

        # Convert 2-D to 1-D array
        oneD = [y for x in mat for y in x]

        # Convert 1-D to 2-D array
        for i in range(r):
            for j in range(c):
                rs[i][j] = oneD[c * i + j]
        return rs