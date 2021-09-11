class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using hashmap
        visited = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in visited:
                return [visited[diff], i+1]
            if num not in visited:
                visited[num]=i+1
        return []
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        # using two pointer
        l = 0
        r = len(numbers)-1
        while l<=r:
            summ = numbers[l]+numbers[r]
            if summ==target:
                return [l+1, r+1]
            if summ>target:
                r-=1
            else:
                l+=1
        return []