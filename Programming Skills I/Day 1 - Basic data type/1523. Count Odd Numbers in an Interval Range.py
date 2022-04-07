class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Using formular: https://www.geeksforgeeks.org/count-odd-and-even-numbers-in-a-range-from-l-to-r/
        # Time O(1)
        # Space O(1)
        n = (high - low +1)
        if n%2==0:
            return n//2
        else:
            if low%2==0 and high%2==0:
                return n//2
            else:
                return n//2 + 1