class Solution:
    def tribonacci(self, n: int) -> int:
        # Approach 1: using array :V
        fib = [0, 1, 1]
        for i in range(3, n+1):
            fib.append(fib[i-1]+fib[i-2]+fib[i-3])
        return fib[n]
        # Approach 2: not using array
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c