class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach 1: DFS Recursive Backtracking
        # Time O(4^n / sqrt(n)) well, if i could explain this complexity, i would already be a mathematician.;)
        # This is the n-th catalan number 2nCn * 1/n+1 -> bounded asymptontically 4^n / n*sqrt(n)
        # Space O(n) -> size of the stack
        # add open -> open<n
        # add close -> open>close
        # valid if close=open=n
        stack = []
        rs = []
        def backtrack(openN=0, closeN=0):
            if openN==closeN==n:
                rs.append("".join(stack))
                return
            # add open parenthese
            if openN<n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            # add close parenthese
            if closeN<openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack()
        return rs