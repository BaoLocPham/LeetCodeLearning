class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach: Deque
        # Time O(n)
        # Space O(n)
        n = len(nums)
        output = []
        l = r = 0
        dq = deque() # only store indexes, monotonically decreasing queue
        while r < n:
            # pop smaller value from deque
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            # if left most value is out of window
            if l > dq[0]:
                dq.popleft()
            
            if r+1 >= k: # append results
                output.append(nums[dq[0]])
                # only update l when size of windows = k
                l += 1
            r += 1
        return output
            