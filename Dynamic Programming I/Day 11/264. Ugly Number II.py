class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Approach 1: DP
        # Time O(n)
        # Space O(n)
        p2, p3, p5 = 0, 0, 0
        k = [0]*n
        k[0] = 1
        for i in range(1, n):
            k[i] = min(k[p2]*2, k[p3]*3, k[p5]*5)
            if k[i]==k[p2]*2: p2+=1
            if k[i]==k[p3]*3: p3+=1
            if k[i]==k[p5]*5: p5+=1
        return k[-1]

    # Approach 2: generate an sorted array of product
    # Simple Precompute and then call the array when ever the function calls
    # So Everytime a function call -> Time O(1) :V
    # Thanks StefanPochmann for this brilliant idea.
    # Time O(n) for precompute
    # Space O(n)
    ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly[n - 1]