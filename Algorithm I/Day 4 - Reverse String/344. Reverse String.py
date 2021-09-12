class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointer approach. :)
        l = 0
        r = len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        # or you just use the python build in function
        # s = s.reverse()