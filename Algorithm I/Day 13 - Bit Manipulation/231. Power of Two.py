class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Approach 1:
        # Concept: because power of two meaning the 2^0 bits is zero
        # 1000 = 8
        # &
        # 0111 = 7
        # -----
        # 0000 
        if n<=0:
            return False
        return n&(n-1)==0
