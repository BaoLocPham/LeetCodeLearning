class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Approach 1: DP
        # travel backwards if word is match then dp[i] = dp[i:i+len(w)]
        # Time O(n)
        # Space O(1)
        dp = [0]*(len(s)+1)
        dp[-1] = 1 # base case
        for i in range(len(s)-1, -1 , -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)] #
                if dp[i]: # if there already a match break inner loop
                    break
        return dp[0] # when all words are matched -> dp[0]=1