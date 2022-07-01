class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Approach sort
        # Time O(nlogn) # sort and traverse the array once
        # Space O(n)
        rs = []
        people.sort(key=lambda x: [-x[0], x[1]]) # sort heigh descending, k increasing
        for p in people:
            rs.insert(p[1], p) # insert by k
        return rs