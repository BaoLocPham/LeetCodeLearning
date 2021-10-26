class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Approach 1: sorting
        # Time O(nlogn)
        # Space O(n)
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # if the list of merged intervals is empty or if the current
                # interval does not overlap with the previous, simply append it.
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged