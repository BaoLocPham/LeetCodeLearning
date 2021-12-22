class Solution:
    def isSubsequence(self, s, t):
        # Approach 1: iteration
        # Time O(n*m)
        # Space O(n)
        t = iter(t)
        return all(c in t for c in s)
        # Approach 2: two pointers
        # Time O(n+m)
        # Space O(1)
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
        return s_i == len(s)
        # Approach 3: Binary searh
        # :V