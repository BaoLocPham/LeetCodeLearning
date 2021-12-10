class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach 1: Brute Force
        # Time O(n^3)
        # Space O(?)
        # yeah, i'm lazy af

        # Approach 2: DP
        # Time O(n^2)
        # Space O(1)
        res, resLen = "", 0
        for i in range(len(s)):
            # odd length substring
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l-=1
                r+=1
            # even length substring
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l-=1
                r+=1
        return res