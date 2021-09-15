class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach 1: using hashMap
        # Time O(n)
        # Space O(n) using hashMap
        # if len(s) <= 1:
        #     return len(s)
        #
        # charMap = dict()
        # start = 0
        # longest = 0
        # for i, c in enumerate(s):
        #     if c in charMap:
        #         start = max(start, charMap[c] + 1)
        #     longest = max(longest, i - start + 1)
        #     charMap[c] = i
        # return longest

        # Approach 2: using Sliding Windows
        # Time O(n)
        # Space O(n)
        charSet = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
        return maxLength