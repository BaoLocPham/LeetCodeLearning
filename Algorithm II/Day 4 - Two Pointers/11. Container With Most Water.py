class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Approach 1: Brute Force -> Time limit exceeded
        # Time O(n^2)
        # Space O(1)
        maxV = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j:
                    continue
                maxV = max(maxV, abs(i - j) * min(height[i], height[j]))
        return maxV
        # Approach 2: Two pointers
        # Time O(n)
        # Space O(1)
        l, r = 0, len(height)-1
        maxV = 0
        while l<r:
            v = (r-l)*min(height[l], height[r])
            maxV = max(maxV, v)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxV