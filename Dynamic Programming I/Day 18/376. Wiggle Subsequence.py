class Solution:
    def wiggleMaxLength(self, nums):
        # Approach 1: No idea, but just pythonic
        # Time O(n)
        # Space O(n)
        nan = float('nan') # for padding 
        # compute differents in neighbor
        diff = [a-b for a, b in zip([nan]+nums, nums+[nan]) if a-b]
        # counts local minima
        return sum(not d*e >= 0 for d, e in zip(diff, diff[1:]))