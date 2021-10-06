class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Basically this problem is similar to problem 78. Subset
        # But it only allow power set
        # When there is no duplicate -> number of of subset N-> 2^N
        # When there is duplicate ->  number of of subset N
        # Given an array (a1, a2, a3, ..., an)
        # with each of them appearing (k1, k2, k3, ..., kn) times,
        # the number of subset is (k1+1)(k2+1)...(kn+1)
        # [1, 2, 2] -> [1,2] -> (1+1)*(2+1) = 2*3 = 6
        # [[], [1], [2], [1,2], [2,2], [1,2,2]] => len = 6
        # Time O(N*2^N) -> without duplicate
        # Space O(n)
        output = []
        n = len(nums)
        nums = sorted(nums)

        def backtrack(first=0, curr=[], k=0):
            # if combination is completed
            if len(curr) == k:
                output.append(curr[:])
                return
                # Continue backtracking
            for i in range(first, n):
                # check duplicate
                if i > first and nums[i] == nums[i - 1]:
                    continue
                # append the nums[i] to the combination
                curr.append(nums[i])
                # use next integer to complete the combination
                backtrack(i + 1, curr, k)
                # backtrack
                curr.pop()

        for k in range(n + 1):
            backtrack(k=k)
        return output
