class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 1: Treat like fibonacci sequences
        # Time O(n)
        # Space O(n)
        # steps=[1,2]
        # for i in range(1, n+1):
        #     steps.append(steps[i]+steps[i-1])
        # return steps[n-1]
        # Approach 2: Use two variable for storing last values
        # Time O(n)
        # Space O(1)
        st1, st2 = 1, 2
        if n <= 2:
            return st1 if n < 2 else st2
        for i in range(2, n):
            tmp = st2
            st2 = st1 + st2
            st1 = tmp
        return st2