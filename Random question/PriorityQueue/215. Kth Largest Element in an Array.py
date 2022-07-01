class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1: Min Heap
        # Time O(nlogk)
        # Space O(k)
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return - heapq.heappop(nums)