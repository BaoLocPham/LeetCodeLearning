class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # Approach 1: not very DP
        # countNeg and find zero index
        # Time O(n)
        # Space O(1)
        # countNeg use to count number of neg from index 0 to current index
        firstNeg, zeroPos, countNeg, maxCount = -1, -1, 0, 0
        for i in range(len(nums)):
            if nums[i]<0:
                countNeg +=1
                if firstNeg==-1: # we only to know first neg index
                    firstNeg = i
            if nums[i]==0: # when cur is 0, we can't use any element from 1 to current anymore
                countNeg=0
                firstNeg=-1
                zeroPos=i
            else: # curr is pos or neg
                # consider index zero
                if countNeg%2==0: # even if neg is pos
                    maxCount = max(i-zeroPos, maxCount)
                else: # even if when there is no neg -> i-firstNeg = number of pos
                    maxCount = max(i-firstNeg, maxCount)
        return maxCount