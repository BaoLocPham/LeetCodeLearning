class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: recursion backtracking
        # Time O(n!?)
        # Space O()
        rs = []
        # Base case
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            nums.append(n)
            rs.extend(perms)
        return rs