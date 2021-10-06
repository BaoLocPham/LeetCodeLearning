class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Cascading
        # Time O(n*2^n) -> copy the list of length at most N at the end of every subset.
        # And there are 2^N subsets in total.
        # Space O(n*2^n) -> This is exactly the number of solutions for subsets
        # multiplied by the number N of elements to keep for each subset.
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr+[num] for curr in output]
        return output

        # Approach 2: Backtracking
        # Time O(n*2^n) -> Same as Cascading
        # Space O(n) -> We are using O(N)O(N) space to maintain curr, and are modifying curr in-place with backtracking.
        n = len(nums)
        output = []
        def backtrack(first=0, curr=[], k=0):
            # if combination is completed
            if len(curr) == k:
                output.append(curr[:])
                return
                # Continue backtracking
            for i in range(first, n):
                # add nums[i] to the current combinations
                curr.append(nums[i])
                # use next integer to complete the combinations
                backtrack(i + 1, curr, k)
                # backtrack
                curr.pop()
        for i in range(n + 1):
            backtrack(k=i)
        return output

        # Approach 3: Lexicographic (Binary Sorted) Subsets
        # Time O(n*2^n)
        # Space O(n*2^n) ->  to keep all the subsets of length NN, since each of NN elements could be present or absent.
        n = len(nums)
        output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output