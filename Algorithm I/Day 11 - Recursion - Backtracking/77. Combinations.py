class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Approach 1: Backtracking
        # Time O(kN^k) -> O(k*n!/(n-k!)k!)
        # Space O(?)
        rs = []
        def backtrack(start, comb):
            if len(comb)==k:
                # because the comb is mutable
                # to append a mutable -> append a copy of it
                rs.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return rs