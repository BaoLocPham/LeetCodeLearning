class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach 1: Sort by end time
        # Time O(nlogn) -> time for sorting the intervals
        # Space O(1)
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]
        for interval in intervals:
            if interval[0]>=end:
                end = interval[1]
                count+=1
        return len(intervals)-count