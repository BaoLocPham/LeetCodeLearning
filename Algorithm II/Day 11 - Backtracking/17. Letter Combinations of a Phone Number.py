class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach 1: DFS Recursive Backtrack
        # Time O(n*4^n) -> worst case
        # Space O(1)
        rs = []
        digitsMap = {
            "2":"acb",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7": "pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(i=0, cur=""):
            if len(cur)==len(digits):
                rs.append(cur)
                return
            for c in digitsMap[digits[i]]:
                dfs(i+1, cur+c)
                # backtracking
        if digits:
            dfs()
        return rs