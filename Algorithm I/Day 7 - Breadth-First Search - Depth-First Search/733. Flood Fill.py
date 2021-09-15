class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # This is an DFS problems

        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        # Approach 1: Using recursion
        # def dfs(r,c):
        #     if image[r][c] == color:
        #         image[r][c] = newColor
        #         if (r+1<R):
        #             dfs(r+1,c)
        #         if (r>0):
        #             dfs(r-1,c)
        #         if (c+1<C):
        #             dfs(r,c+1)
        #         if (c>0):
        #             dfs(r,c-1)
        # dfs(sr, sc)

        # Approach 2: Iterative
        stack = [(sr, sc)]
        while (stack):
            i, j = stack.pop()
            if image[i][j] == color:
                image[i][j] = newColor
                if i + 1 < R:
                    stack.append((i + 1, j))
                if i > 0:
                    stack.append((i - 1, j))
                if j + 1 < C:
                    stack.append((i, j + 1))
                if j > 0:
                    stack.append((i, j - 1))
            else:
                continue
        return image