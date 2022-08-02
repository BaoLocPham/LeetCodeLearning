import string
from collections import Counter
class Solution:
    # Approach: Counter
    # Time O(N+M) N is len of words1, M is len of words2
    # Space O(N+M)
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        rs = []
        # max_b_frequency = dict(zip(string.ascii_lowercase, [0]*26))
        max_b_frequency = [0]*26
        
        for w2 in words2: # create a counter for words2 # subset
            frequency = self.countFrequency(w2)
            for i in range(0, 26):
                max_b_frequency[i] = max(max_b_frequency[i], frequency[i])
                
        for w1 in words1:
            frequency = self.countFrequency(w1)
            flag = True
            for i in range(0, 26):
                if max_b_frequency[i]>frequency[i]:
                    flag = False
                    break
            if flag:
                rs.append(w1)
        return rs
    
    def countFrequency(self,word):
        frequency = [0]*26
        for w in word:
            frequency[ord(w)-ord('a')] += 1
        return frequency
    
    