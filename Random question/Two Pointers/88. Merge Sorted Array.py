class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time O(m+n)
        # Space O(m) # tmp array
        tmp_nums1 = nums1[:m]
        
        p1, p2 = 0, 0
        for p in range(m+n):
            if p2>=n or (p1<m and tmp_nums1[p1]<=nums2[p2]) :
                nums1[p] = tmp_nums1[p1]
                p1+=1
            else:
                nums1[p] = nums2[p2]
                p2+=1
                
        # Time O(m+n)
        # Space O(1) 
        last = m+n-1
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1