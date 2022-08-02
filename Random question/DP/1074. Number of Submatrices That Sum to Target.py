class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Refer to 560. Subarray Sum Equals K
        # Time O(mnn) 
        # Space O(m)
        if not matrix or not matrix[0]:
            return 0

        presum = list(map(lambda row: list(itertools.accumulate(row)), matrix))

        rows, cols = len(matrix), len(matrix[0])

        count = 0
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                counter = collections.Counter()
                counter[0] = 1
                curr_sum = 0
                for r in range(rows):
                    curr_sum += presum[r][col_end] - (presum[r][col_start - 1] if col_start else 0)
                    count += counter[curr_sum - target]
                    counter[curr_sum] += 1
        return count