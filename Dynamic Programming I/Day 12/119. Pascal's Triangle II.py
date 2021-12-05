class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Approach 1: DP same as Pascal Triangle I
        # Time O(n^2)
        # Space O(n)
        
        # Approach 2: DP
        # Time O(n)
        # Space O(n)
        A = [0] * (rowIndex + 1)
        A[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                A[j] += A[j - 1]
        return A
