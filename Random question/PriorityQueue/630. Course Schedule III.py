class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Max heap approach
        # Time O(nlogn*n)
        # Space O(n)
        heap = []
        start = 0
        courses = sorted(courses, key = lambda x:x[1])
        for t, end in courses:
            start += t
            heapq.heappush(heap, -t)
            while start>end:
                start += heapq.heappop(heap)
        return len(heap)
            