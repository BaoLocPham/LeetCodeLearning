class Solution:
    def isUgly(self, n: int) -> bool:
        # This is not a dp problem
        # Time O(n)
        # Space O(1)
        for i in 2, 3, 5:
            while n%i==0<n:
                n/=i
        return n==1