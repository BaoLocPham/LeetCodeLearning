class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Approach 1: Greedy
        # Time O(n)
        # Space O(1) -> array for storing the last
        last = [0]*26
        for i,char in enumerate(s):
            last[ord(char)-ord('a')] = i
        j, anchor = 0, 0
        ans = []
        for i in range(len(s)):
            j = max(j, last[ord(s[i])-ord('a')])
            if i==j:
                ans.append(j-anchor+1)
                anchor = i+1
        return ans