class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach DP:
        # Time O(n*n) # n loop over position in s, n for checking palindrome
        # Space O(n) 
        res, resLen = "", 0
        n = len(s)
        for i in range(n):
            # odd length substring
            l, r = i, i
            while 0<=l and r<n and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l-=1
                r+=1
                
            # even length substring
            l, r = i, i+1
            while 0<=l and r<n and s[l]==s[r]:
                if r-l+1>resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l-=1
                r+=1
        return res