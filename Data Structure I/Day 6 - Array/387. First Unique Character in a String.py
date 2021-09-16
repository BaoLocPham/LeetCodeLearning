class Solution:
    def firstUniqChar(self, s: str) -> int:
        # using hashMap to count number of appearance in the string
        # Time O(n)
        # Space O(n) size of hashMap
        # Approach 1: build an hashMap from scratch
        # count = dict()
        # for c in s:
        #     if c in count:
        #         count[c] += 1
        #     else:
        #         count[c] = 1
        # for i, c in enumerate(s):
        #     if count[c]==1:
        #         return i
        # return -1
        # Approach 2: using Counter from collections python
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

