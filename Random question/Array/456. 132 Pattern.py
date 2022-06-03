class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Approach: stack
        # Time O(n)
        # Space O(n)
        stack = [] # (num, minLeft), mono decreasing
        curMin = nums[0]
        
        for n in nums[1:]:
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack and n<stack[-1][0] and n>stack[-1][1]:
                return True
            
            stack.append([n, curMin])
            curMin = min(curMin, n)
            
        return False