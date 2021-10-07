class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1: Backtracking Recurisve DFS
        # Time O(n*m)
        # n: #elements each level of recursive tree, m: height of the recursive tree
        # Space O(m)
        rs = []
        def dfs(i=0, cur=[], total=0):
            # the base case
            if i>=len(candidates) or total>target:
                return
            # when total value equal target
            if total==target:
                rs.append(cur.copy())
                return
            # we have two choices
            # Include or don't include the candidates[i]
            # 1. Include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            # 2. Don't include candidates
            cur.pop()
            dfs(i+1, cur, total)
        dfs()
        return rs