class Solution:
    # Approach 1: Recursion
    # Time O(2^n) TLE :(
    # Space O(?)
    # def numDecodings(self, s: str) -> int:
    #     return 0 if len(s) == 0 else self.solve(0, s)
    # def solve(self, p: int, s: str) -> int:
    #     n = len(s)
    #     if p == n:
    #         return 1
    #     if s[p] == "0":  # substring start with 0 is not a valid substring
    #         return 0
    #     # substring with len=1
    #     res = self.solve(p + 1, s)
    #     # substring with len=2
    #     if p < n - 1 and (s[p] == '1' or (s[p] == '2' and s[p + 1] < '7')):
    #         res += self.solve(p + 2, s)
    #     return res

    # Approach 2: Recursion + Memorization
    # Time O(n)
    # Space O(n)
    def numDecodings(self, s: str) -> int:
        def solve(p: int, s: str) -> int:
            if mem[p] > -1: return mem[p]
            if s[p] == "0":  # substring start with 0 is not a valid substring
                mem[p] = 0
                return mem[p]
            # substring with len=1
            res = solve(p + 1, s)
            # substring with len=2
            if p < n - 1 and (s[p] == '1' or (s[p] == '2' and s[p + 1] < '7')):
                res += solve(p + 2, s)
            mem[p] = res
            return res
        n = len(s)
        mem = [-1] * (n + 1)
        mem[-1] = 1
        return 0 if n == 0 else solve(0, s)

    # Approach 3: DP
    # Time O(n)
    # Space O(n)
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mem = [-1] * (n + 1)
        mem[-1] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                mem[i] = 0
            else:
                # len=1
                mem[i] = mem[i + 1]
                # len=2
                if i < n - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] < "7")):
                    mem[i] += mem[i + 2]
        return 0 if s == "" else mem[0]

    # Approach 4: DP
    # Time O(n)
    # Space O(n)
    # It easy when you know how to solve this