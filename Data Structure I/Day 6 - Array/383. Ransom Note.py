class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # This problem is just straightforward
        # Approach 1: using hashMap or whatever you want to use to count
        # Time O(n)
        # Space O(n) space of two hashMap
        # ranDict = [0]*26
        # magDict = [0]*26
        # for c in magazine:
        #     magDict[ord(c)-ord('a')]+=1
        # for c in ransomNote:
        #     ranDict[ord(c)-ord('a')]+=1
        # for i, c in enumerate(ransomNote):
        #     if ranDict[ord(c)-ord('a')]> magDict[ord(c)-ord('a')]:
        #         return False
        # return True
        # Approach 2: Using counter subtraction in python collection
        # Return empty Counter if all of the element in a is subtracted
        # Time O(n)
        # Space O(n)
        a = collections.Counter(ransomNote)
        b = collections.Counter(magazine)
        return not a-b
