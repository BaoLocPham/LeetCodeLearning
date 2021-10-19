class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Approach 1: Bitwise
        # Time O(n)
        # Space O(1)
        count = 0
        while left != right:
            left >>=1
            right >>=1
            count+=1
        return left<<count