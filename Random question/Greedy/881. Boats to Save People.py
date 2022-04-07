class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Greedy
        # Time O(n)
        # Space O(1)
        l, r = 0, len(people)-1
        people.sort()
        
        count = 0
        while l<=r:
            if l==r:
                count+=1
                break
            if people[l] + people[r] <= limit:
                l, r = l+1, r-1
            else:
                r -= 1
            count+=1
        return count