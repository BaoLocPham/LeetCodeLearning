class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Approach 1: Official's solution
        # For me, this approach is hard to follow
        # Time O(n)
        # Space O(n)
        n = len(nums)
        maxEnd = maxSoFar = -3e4 - 1  # yeah because the problem state that
        for num in nums:
            maxEnd = num + max(maxEnd, 0)
            maxSoFar = max(maxSoFar, maxEnd)
        # maxSoFar is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])
        rightsums = [None] * n
        rightsums[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + nums[i]

        # maxright[i] = max_{j>=i} rightsums[j]
        maxright = [None] * n
        maxright[-1] = rightsums[-1]
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])

        leftsum = 0
        for i in range(n - 2):
            leftsum += nums[i]
            maxSoFar = max(maxSoFar, leftsum + maxright[i + 2])
        return maxSoFar

        # Approach 2: One-pass
        # You have two case:
        # 1. the max subsequence is inside the array
        # 2. the max subsequence is take part as head of the array and tail of the array
        # -> you can think of we can find the max of the maxSum of case 1 and total-minSum
        # Time O(n)
        # Space O(1)
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(curMax, maxSum)
            curMin = min(curMin + num, num)
            minSum = min(curMin, minSum)
            total += num
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum