class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Approach 1: Recursion backtracking
        # Time O(2^N)
        # Space O(?)
        def backtrack(sub="", i=0):
            if i == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
        res = []
        backtrack()
        return res