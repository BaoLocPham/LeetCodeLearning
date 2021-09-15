class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            head = matrix[mid][0]
            tail = matrix[mid][-1]
            if head == target or tail==target:
                return True
            elif head<target and tail>target:
                break
            elif head > target:
                bot = mid-1
            else:  # val<target
                top = mid + 1
        row = mid
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (right + left) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:  # val>target
                right = mid - 1
        return False