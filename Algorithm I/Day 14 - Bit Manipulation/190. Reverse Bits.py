class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Concept is the same:
        - Loop 32 times:->problem state that 32bit integer.
        - result is shift to the left 1 bits
        - if the right most bit in number is 1 -> plus 1 to the result
        - shift the number to the right 1 bits, because we done with that right most bit.
        return result
        """
        # Time O(n) 
        # Space O(1)
        reverse = 0
        for i in range(0, 32):
            reverse = reverse<<1
            if n&1==1:
                reverse = reverse ^ 1
            n = n>>1
        return reverse