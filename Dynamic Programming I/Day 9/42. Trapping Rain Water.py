class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1: Brute Force # TLE :))
        # Time O(n^2)
        # Space O(1)
        accumulate = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            accumulate += min(max_left, max_right) - height[i]
        return accumulate

        # Approach 2: DP
        # similar to Trapping rain water I
        # Time O(n)
        # Space O(n)
        n = len(height)
        if n <= 1:
            return 0
        # the vol = min(right, left)-height
        right_max, left_max = [0] * n, [0] * n

        # find left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # find right_max
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        vol = 0
        # find vol
        for i in range(n):
            vol += min(left_max[i], right_max[i]) - height[i]
        return vol
