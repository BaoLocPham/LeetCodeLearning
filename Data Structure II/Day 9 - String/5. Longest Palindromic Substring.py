class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(n^2)
        res = ""
        resLen = 0
        # check every character
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            # even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res