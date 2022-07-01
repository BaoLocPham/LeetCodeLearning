class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # min heap
        # Time O(nlogk)
        # Space O(k)
        heap = []
        for i in range(len(heights) - 1):
            distance = heights[i+1] - heights[i]
            if distance > 0: # using ladders
                heapq.heappush(heap, distance)
            if len(heap) > ladders: # using breaks instead
                bricks -= heapq.heappop(heap) # switch using bricks for the smallest distance
                # or using ladder of the largest distance
            if bricks < 0:
                return i
        return len(heights) - 1