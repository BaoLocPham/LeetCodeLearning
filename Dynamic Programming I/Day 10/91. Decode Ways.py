class Solution:
    # Approach 1: Brute Forces Recursive -> TLE
    # Time O(n^2)
    # Space O(1)
    def numDecodings(self, s: str) -> int:
        return 0 if len(s)==0 else self.decode(0, s)
    def decode(self, p:int , s: str):
        n = len(s)
        if p==n: # base case
            return 1
        if s[p]=='0': # start with zero is not a valid decode
            return 0
        res = self.decode(p+1, s)
        if p<n-1 and (s[p]=='1' or (s[p]=='2' and s[p+1]<'7')):
            res += self.decode(p+2, s)
        return res

    # Approach 2: DP Recursive memoization
    # Time O(n)
    # Space O(n)
    def numDecodings(self, s: str) -> int:
        mem = [-1] * (len(s) + 1)
        mem[-1] = 1 # base case
        return 0 if len(s) == 0 else self.decode(0, s, mem)

    def decode(self, p: int, s: str, mem: [int]):
        n = len(s)
        if mem[p] > -1:
            return mem[p]
        if s[p] == '0':  # start with zero is not a valid decode
            mem[p] = 0
            return mem[p]
        res = self.decode(p + 1, s, mem)
        if p < n - 1 and (s[p] == '1' or (s[p] == '2' and s[p + 1] < '7')):
            res += self.decode(p + 2, s, mem)
        mem[p] = res
        return res

    # Approach 3: DP Iterative memoization
    # Time O(n)
    # Space O(n)
    n = len(s)
    dp = [-1] * (n + 1)
    dp[-1] = 1
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                dp[i] += dp[i + 2]
    return dp[0]

    # Approach 3: DP Iterative with constant space
    # Space O(n)
    # Space O(1)
    n = len(s)
    p, pp = 1, 0
    for i in range(n - 1, -1, -1):
        cur = 0 if s[i] == '0' else p
        if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
            cur += pp
        pp = p
        p = cur
    return 0 if n == 0 else p