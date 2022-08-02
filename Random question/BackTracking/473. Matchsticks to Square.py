class Solution:
    # Approach: Backtracking
    # Time O(4^n) # 4 edges and worst case is go n elements in the array
    # Space O(?)
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != length:
            return False
        
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4): # 4 sides of a square
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1): # check next matchsticks
                        return True
                    sides[j] -= matchsticks[i]
                    if i == 0: 
                    # if the first matchsticks is not qualify then
                    # do not need to loop through all four sides as a starting side
                        return False
            return False
    
        return backtrack(0)