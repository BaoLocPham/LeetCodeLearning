import heapq as hp
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Sorting 
        # Time O(n*m*logn)
        # Space O(n)
        arr = []
        m, n = len(mat), len(mat[0])
        for r in range(m):
            arr.append((sum(mat[r]), r))
        arr.sort()
        return [x[1] for x in arr[:k]]
            
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Min heap + binary search
        # Time O(m*(logn+logk)) 
        # Space O(n)
        minHeap = [(self.countOnes(mat[i]), i) for i in range(len(mat))]
        hp.heapify(minHeap)
        
        return [hp.heappop(minHeap)[1] for _ in range(k)] 
    
    def countOnes(self, nums:List[int])->int:
        l, r = 0, len(nums)
        while l<r:
            mid = (l+r)>>1
            if nums[mid]==1:
                l=mid+1
            else:
                r=mid
        return l