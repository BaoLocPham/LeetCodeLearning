class Solution:
    # Approach 1: DP
    # we can preprocess the problem and then it turn to house robber I again
    # nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
    # points: [0, 0, 4, 9, 4] <- This is the gold in each house!
    # Time O(n)
    # Space O(n)
    def deleteAndEarn(self, nums: List[int]) -> int:
        def house_robber_solver(house):
            prev1, prev2 = 0, 0
            for num in house:
                prev2, prev1 = prev1, max(prev1, prev2+num)
            return prev1
        points = [0]*10001
        for num in nums:
            points[num] += num
        return house_robber_solver(points)

    # Approach 2: Still DP but only 4 lines  ¯\_(ツ)_/¯
    # Time O(n)
    # Space O(n)
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev2, prev1, counter = 0, 0, Counter(nums)
        for value in range(max(counter.keys()) + 1):
            prev2, prev1 = prev1, max(prev2 + value * counter[value], prev1)
        return prev1
