class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 1: basically fibonacci
        # Time O(n)
        # Space O(1)
        st1, st2 = 1, 2
        if n < 2:
            return st1 if n < 2 else st2
        for i in range(2, n):
            tmp = st1 + st2
            st1, st2 = st2, tmp
        return st2
        
        # Approach 2: more brilliant
        st1, st2 = 1, 1
        for i in range(n):
            st1, st2 = st2, st1+st2
        return st1