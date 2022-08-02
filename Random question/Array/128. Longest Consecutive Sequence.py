class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time O(n^3) # two nested loop and the finding cost O(n)
        # Space O(1)
        if not nums:
            return 0
        num_set = set(nums)
        longest_streak = 1
        for num in nums:
            current_num = num
            current_streak = 1
            while current_num +1 in num_set:
                current_streak += 1
                current_num += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
        
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach: HashMap 
        # Time O(n) # only check number once, hashset only cost O(1) to look up
        # Soace O(n) # hash set
        if not nums:
            return 0
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num +1 in num_set:
                    current_streak += 1
                    current_num += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
        
        def longestConsecutive(self, nums):
            # Approach: sorting
            # Time O(nlogn) # the main loop not always run n times, so just the sorting
            # Space O(1)
            if not nums:
                return 0

            nums.sort()

            longest_streak = 1
            current_streak = 1

            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    if nums[i] == nums[i-1]+1:
                        current_streak += 1
                    else:
                        longest_streak = max(longest_streak, current_streak)
                        current_streak = 1

            return max(longest_streak, current_streak)