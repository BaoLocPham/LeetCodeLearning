class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Approach: Implementation
        # Time O(n) # two passes + sum
        # Time O(n)
        rs = [1]*len(ratings)
        
        # check left
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                rs[i] = rs[i-1]+1
        
        # check right
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rs[i] = max(rs[i], rs[i+1] + 1)
        
        return sum(rs)
            