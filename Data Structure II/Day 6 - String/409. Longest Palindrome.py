class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Approach 1: Greedy
        # Time O(n)
        # Space O(n)
        
        count = {}
        for c in s:
            count[c] = count.get(c, 0)+1
        ans = 0
        for c, v in count.items():
            ans += v//2*2
            # if there is a unique character
            if ans%2==0 and v%2==1:
                ans+=1
        return ans