class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Approach 1: DP
        # Time O(n*m)
        # Space O(n*m)
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        l1, l2 = len(word1), len(word2)
        # fill up bottom row
        for j in range(l2 + 1):
            cache[l1][j] = l2 - j

        for i in range(l1 + 1):
            cache[i][l2] = l1 - i

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        return cache[0][0]
