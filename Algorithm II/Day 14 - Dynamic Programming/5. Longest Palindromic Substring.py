class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach 1: DP
        # Time O(n^2) Time for spaning every single character windows
        # Space O(1)
        res = ""
        resLen = 0
        # check every character
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

        # Approach 2: Manacher's Algorithm
        # Time O(n)
        # Space O(n)
        # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
        # This algorithm is not trivial ¯\_(ツ)_/¯
