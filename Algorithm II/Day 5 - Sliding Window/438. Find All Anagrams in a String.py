class Solution:
    def makeCounter(self, s):
        dd = {}
        for char in s:
            dd[char] = dd.get(char, 0) + 1
        return dd

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Approach 1: Sliding windows
        # Time O(n)
        # Space
        dictP = self.makeCounter(p)
        dictS = self.makeCounter(s[:len(p)])
        rs = []
        for i in range(0, len(s) - len(p) + 1):
            if dictP == dictS:
                rs.append(i)
            # Decrease the count of oldest char in the window
            dictS[s[i]] -= 1
            # If the count of the char is 0 -> remove that char
            if dictS[s[i]] == 0:
                del dictS[s[i]]
            # Check if next index is valid
            if i + len(p) < len(s):
                dictS[s[i + len(p)]] = dictS.get(s[i + len(p)], 0) + 1
        return rs
