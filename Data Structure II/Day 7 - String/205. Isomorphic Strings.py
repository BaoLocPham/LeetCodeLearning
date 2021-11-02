class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # This problem is similar to 290. Word Pattern problem
        # Time O(n)
        # Space O(n)
        s_to_t = [-1]*256
        t_to_s = [-1]*256
        for i in range(len(s)):
            c1, c2 = ord(s[i]), ord(t[i])
            # Case 1: no exist mapping in either of the dictionaries
            if s_to_t[c1]==-1 and t_to_s[c2]==-1:
                s_to_t[c1]=c2
                t_to_s[c2]=c1
            # Case 2: There are exist mapping but doesn't math in both of the dictionaries
            elif not (s_to_t[c1]==c2 and t_to_s[c2]==c1):
                return False
        return True