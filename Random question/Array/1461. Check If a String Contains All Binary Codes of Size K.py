class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Time O(n)
        # Space O(n)
        # The idea just simple check if the dict have the same elements as the numberOfCodes
        numberOfCodes = 2**k
        n = len(s)
        count = set()
        for i in range(n-k+1):
            count.add(s[i:i+k])
            if len(count)==numberOfCodes:
                return True
        return False