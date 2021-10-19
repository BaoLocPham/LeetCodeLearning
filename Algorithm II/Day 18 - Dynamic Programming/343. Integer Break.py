class Solution:
    def integerBreak(self, n: int) -> int:
        # Approach 1: Recursion Memoize
        # Time O(?)
        # Space O(?)
        memoize = {}
        def solve(num:int)->int:
            if num<=2:
                return 1
            if num in memoize:
                return memoize[num]
            ans = 1*(num-1)
            for i in range(2, num):
                firstNum = i
                secondNum = num-i
                product = firstNum * max(secondNum, solve(secondNum))
                if product > ans:
                    ans = product
            memoize[num] = ans
            return ans
        ans = solve(n)
        return ans

        # Approach 2: Implementation
        # Time O(n)
        # Space O(1)
        if n == 2: return 1
        if n == 3: return 2
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans