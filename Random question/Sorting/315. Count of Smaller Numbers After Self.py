class Element:
    def __init__(self, val, indx):
        self.val = val
        self.indx = indx
        
class Solution:
    
    # Approach: Merge Sort
    # Time O(nlogn)
    # Space O(n)
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        rs = [0]*n
        array_of_elements = []
        for i in range(n):
            array_of_elements.append(Element(nums[i], i))
        
        self.mergeSortAndCount(array_of_elements, 0, n-1, rs)
        
        return rs
    
    def mergeSortAndCount(self, array_of_elements, start, end, rs):
        if start >= end:
            return None
        
        mid = (start+end)//2
        
        self.mergeSortAndCount(array_of_elements, start, mid, rs)
        self.mergeSortAndCount(array_of_elements, mid+1, end, rs)
        
        leftPos = start
        rightPos = mid + 1
        
        merged = []
        num_rights_smaller_than_left = 0
        
        while leftPos < mid + 1 and rightPos <= end:
            if array_of_elements[leftPos].val > array_of_elements[rightPos].val:
                # this code block is exactly what the problem is asking us for:
                # a number from the right side of the original input array, is smaller
                # than a number from the left side
                #
                # within this code block,
                # array_of_elements[rightPos] is smaller than the start of the left sub-array.
                # Since left sub-array is already sorted,
                # array_of_elements[rightPos] must also be smaller than the entire remaining left sub-array
                num_rights_smaller_than_left += 1
                
                # continue with normal merge sort, merge
                merged.append(array_of_elements[rightPos]);
                rightPos += 1
            else:
                rs[array_of_elements[leftPos].indx] += num_rights_smaller_than_left
                
                merged.append(array_of_elements[leftPos])
                leftPos += 1
                
        while leftPos < mid + 1:
            rs[array_of_elements[leftPos].indx] += num_rights_smaller_than_left
            
            merged.append(array_of_elements[leftPos])
            leftPos += 1
            
        while rightPos <= end:
            merged.append(array_of_elements[rightPos])
            rightPos += 1
        
        pos = start
        for m in merged:
            array_of_elements[pos] = m
            pos += 1
        # for i in range(len(array_of_elements)):
        #     print(array_of_elements[i].val, end=" ")
        # print("")