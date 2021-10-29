class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Approach 1: Brute force
        # Time O(n^3)
        # Space O(1)
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if sum(nums[i:j])==k:
        #             count+=1
        # return count

        # Approach 2: Memoization
        # Time O(O^2)
        # Space O(n)
        # Basic idea is to store the cumulative from 0->j at cumulative[i]
        # When you want to get sum[i:j] = sum[j]-sum[j]
        # count = 0
        # n = len(nums)
        # cumulative = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     cumulative[i] = cumulative[i - 1] + nums[i - 1]
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if cumulative[j] - cumulative[i] == k:
        #             count += 1
        # return count

        # Approach 3: Without Space
        # Time O(O^2)
        # Space O(n)
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     sum = 0
        #     for j in range(i, n):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count

        # Approach 3: HashMap
        # Time O(n)
        # Space O(n)
        # hashMap store (sum i,no.of occurrences of sum i)
        # we update count every time sum-k in hashMap and num=k
        hashMap = {0: 1}
        n = len(nums)
        count = 0
        sum = 0
        for num in nums:
            sum += num
            if hashMap.get((sum - k), 0) != 0:
                count += hashMap.get(sum - k)
            hashMap[sum] = hashMap.get(sum, 0) + 1
        return count