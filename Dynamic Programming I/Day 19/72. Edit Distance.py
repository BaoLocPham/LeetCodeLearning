class Solution:
    # Approach 1: Recursion TLE :((
    # Time O(n^m)
    # Space O(?)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        elif word1[0]==word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, delete, replace)


    # Approach 2: Recursion with memoi
    # Time O(n*m)
    # Space O(n*m)
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memoi = {}
        rs = self.minDistanceHelper(word1, word2, 0, 0, memoi)
        return rs

    def minDistanceHelper(self, word1, word2, i, j, memoi):
        if i == len(word1) and j == len(word2):
            return 0
        elif i == len(word1):
            return len(word2) - j
        elif j == len(word2):
            return len(word1) - i
        if (i, j) not in memoi:
            if word1[i] == word2[j]:
                ans = self.minDistanceHelper(word1, word2, i + 1, j + 1, memoi)
            else:
                insert = 1 + self.minDistanceHelper(word1, word2, i, j + 1, memoi)
                delete = 1 + self.minDistanceHelper(word1, word2, i + 1, j, memoi)
                replace = 1 + self.minDistanceHelper(word1, word2, i + 1, j + 1, memoi)
                ans = min(insert, delete, replace)
            memoi[(i, j)] = ans
        return memoi[(i, j)]

    # Approach 3: DP
    # Time O(n*m)
    # Space O(n*m)
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
