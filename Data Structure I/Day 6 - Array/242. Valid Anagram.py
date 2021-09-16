class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This problem is just straightforward
        # Approach 1: Compare between two sum hash
        # Time O(n)
        # Space O(n)
        # ss = sum([hash(c) for c in s])
        # tt = sum([hash(c) for c in t])
        # return True if ss-tt==0 else False
        # Approach 2: using collections Counter
        return collections.Counter(s) == collections.Counter(t)