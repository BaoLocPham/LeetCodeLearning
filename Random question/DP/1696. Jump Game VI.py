class Solution:
    # https://leetcode.com/problems/jump-game-vi/discuss/1260843/C%2B%2BJavaPython-DP-and-Decreasing-Deque-Clean-and-Concise-Time-O(N)-Space-O(K)
    # Approach Naive DP
    # Time O(N*K) TLE
    # Space O(N)
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-math.inf] * n
        dp[0] = nums[0]
        for i in range(n):
            for j in range(max(i-k, 0), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[-1]
        
    # Approach: DP Decreasing Deque
    # Time O(N) # only get the largest value
    # Space O(N)
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque([0])  # store index of `nums` elements, elements is in decreasing order, the front is the maximum element.
        for i in range(1, n):
            # nums[i] = max(nums[i-k], nums[i-k+1],.., nums[i-1]) + nums[i] = nums[dq.front()] + nums[i]
            nums[i] = nums[dq[0]] + nums[i]
            
            # add nums[i] to deque
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            
            # Remove if the last element is out of window size k
            if i - dq[0] >= k:
                dq.popleft()
                
        return nums[-1]