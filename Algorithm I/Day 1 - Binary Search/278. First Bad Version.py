# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while l<=r:
            mid = l+(r-l)//2
            check = isBadVersion(mid)
            if check and isBadVersion(mid-1)==False:
                return mid
            if check:
                r = mid-1
            if not check:
                l = mid+1