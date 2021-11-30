class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Approach 1: DP
        # Time O(n)
        # Space O(1)
        rs=cur=0 # cur -> cur max
        # rs = max([j]+[i]+i-j)
        for v in values:
            rs = max(rs, cur+v)
            # next step the rs will be decrease by 1
            cur = max(v, cur)-1
        return rs

        # Approach 2: DP
        # Time O(n)
        # Space O(1)
        rs=imax=0 # imax = maxV + indexMaxV
        for i,v in enumerate(values):
            # max-> maxV + indexMaxV+current-indexCurrent
            rs = max(rs, imax+v-i)
            imax = max(imax, v+i)
        return rs