class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Approach: Two pointers
        # Time O(n)
        # Space O(n) -> size of rs array
        i = j = 0
        rs = []
        while i<len(firstList) and j<len(secondList):
            h0 = max(firstList[i][0], secondList[j][0])
            l1 = min(firstList[i][1], secondList[j][1])
            if h0<=l1:
                rs.append([h0, l1])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return rs