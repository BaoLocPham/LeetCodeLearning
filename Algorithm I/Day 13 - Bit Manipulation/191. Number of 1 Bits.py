class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1:
        # Concept: shift the n until it become zero while counting the last bit
        count=0
        while n>0:
            if n^1==(n-1):
                count+=1
            n = n>>1
        return count