class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Approach 1: Two pointers
        # Time O(n)
        # Space O(1)
        l, r = 0, len(numbers)-1
        while l<=r:
            diff = target-numbers[l]-numbers[r]
            if diff==0:
                return [l+1, r+1]
            elif diff>0: # value l+r is small
                l +=1
            else:
                r -= 1
        return []