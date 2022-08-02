class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Time O(nlogn) # sort and traverse once
        # Space O(1)        
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        for box, unit in boxTypes:
            if truckSize>box:
                truckSize-=box
                boxes+=box*unit
            else:
                boxes+=truckSize*unit
                return boxes
        return boxes