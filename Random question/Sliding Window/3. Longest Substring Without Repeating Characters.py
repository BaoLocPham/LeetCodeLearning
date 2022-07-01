class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time O(n)
        # Space O(n)
        if len(s)<=1:
            return len(s)
        # Hashmap
        charMap = dict()
        start, longest = 0, 0
        for i, c in enumerate(s):
            if c in charMap:
                start = max(start, charMap[c]+1)
            longest = max(longest, i-start+1) 
            charMap[c] = i
        return longest
        
        # Sliding windows
        charSet = set()
        l, maxLength = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
        return maxLength