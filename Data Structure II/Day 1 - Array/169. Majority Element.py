class Solution:
    def majorityElement(self, nums):
        # Approach 1: Brute Force
        # Time O(n^2)
        # Space O(1)
        # majority_count = len(nums)//2
        # for num in nums:
        #     count = sum(1 for elem in nums if elem == num)
        #     if count > majority_count:
        #         return num

        # Approach 2: HashMap
        # Time O(n)
        # Space O(n)
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # return max(count.keys(), key=count.get)

        # Approach 3: Sorting
        # Time O(n*logn)
        # Space O(1)
        # nums.sort()
        # return nums[len(nums) // 2]

        # Approach 4: Boyer-Moore Voting Algorithm
        # Time O(n)
        # Space O(1)
        count = 0
        candiate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate