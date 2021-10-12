class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Approach 1: Brute Force Decision Tree
        # Time O(2^n) -> TLE :((
        # Space O(?)
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            dp = [False] * (len(s) + 1)
            dp[-1] = True  # base case

            def solve(s: str):
                if len(s) == 0:
                    return True
                for i in range(1, len(s) + 1):
                    if s[0:i] in wordDict and solve(s[i:]):
                        return True
                return False
            return solve(s)

        # Approach 2: DP
        # Time O(n)
        # Space O(n)
        dp = [False]*(len(s)+1)
        dp[-1] = True # base case
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # if there is a match
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]: # if already a match -> break the inner loop dude
                    break
        return dp[0]