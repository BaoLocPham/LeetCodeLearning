class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in visited:
                return [visited[difference], i]
            else:
                visited[num] = i