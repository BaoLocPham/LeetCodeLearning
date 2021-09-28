class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: Binary Search
        # This problem is basically binary search two times
        # First find the row that the value maybe in
        # Second find the value in the row
        # Time O(logn)
        # Space O(1)
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            head, tail = matrix[mid][0], matrix[mid][-1]
            if head == target or tail == target:
                return True
            elif head < target and tail > target:
                break
            elif head > target:
                bot = mid - 1
            else:  # head<target
                top = mid + 1
        row = mid
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:  # val>target
                r = mid - 1
        return False
