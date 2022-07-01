class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        # Approach 1: Implementation
        # O(nlogMaxA)
        # Space O(MaxA)
        sumV, maxIndx = 0, 0
        for i in range(len(target)):
            sumV += target[i]
            if target[maxIndx] < target[i]:
                maxIndx = i
                
        diff = sumV - target[maxIndx]

        if target[maxIndx] == 1 or diff == 1: 
            return True
        
        if diff > target[maxIndx] or diff ==0 or target[maxIndx] % diff == 0:
            return False
        
        target[maxIndx] %=  diff
        
        return self.isPossible(target)
        
    def isPossible(self, target: List[int]) -> bool:
        # Approach 2: Priority Queue
        # Time O(n + logMaxAlogn) n: build priority queue, logMaxAlogn reduce value
        # Space O(n)
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        
        while True:
            maxV = -heapq.heappop(heap)
            total -= maxV
            
            if maxV == 1 or total == 1:
                return True
            
            if maxV < total or total == 0 or maxV % total == 0:
                return False
            
            maxV %= total
            total += maxV
            heapq.heappush(heap, -maxV)
            