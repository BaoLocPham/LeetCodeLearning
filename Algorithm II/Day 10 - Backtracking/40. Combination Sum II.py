class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1: DFS Recursive Backtracking Index
        # Time O(2^n)
        # In the worst case, our algorithm will exhaust all possible combinations from the input array,
        # which in total amounts to 2^N
        # Space O(n) -> cur keep track of combinations
        candidates.sort()
        rs = []
        def dfs(start=0, cur=[], total=0):
            # base case
            if total > target:
                return
            # when total == target -> append the combination
            if total == target:
                rs.append(cur.copy())
                return
            # keep track of prev
            prev = -1
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate == prev:
                    continue
                cur.append(candidate)
                dfs(i + 1, cur, total + candidate)
                cur.pop()
                prev = candidate

        dfs()
        return rs
        # Approach 2: DFS Recursive Backtracking HashMap Counter
        # To be continue, my head is overloadded :((
        


