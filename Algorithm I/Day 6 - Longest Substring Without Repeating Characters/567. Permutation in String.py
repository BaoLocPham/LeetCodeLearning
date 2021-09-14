class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Concept: Two array is anagram when theirs hash score are equals
        # Approach 1: Using hashMap and two pointers
        # Time O(n)
        # Space O(n) -> two hashMap :)
        # hash1 = [0]*26 # this approach is using hashMap of 26 characters indexes
        # hash2 = [0]*26
        # if len(s2)<len(s1):
        #     return False
        # right = left = 0
        # while right<len(s1):
        #     hash1[ord(s1[right])-ord('a')] +=1
        #     hash2[ord(s2[right])-ord('a')] +=1
        #     right+=1
        # right-=1
        # while right<len(s2):
        #     if hash1 == hash2:
        #         return True
        #     right+=1
        #     if right!=len(s2):
        #         hash2[ord(s2[right])-ord('a')] +=1
        #     # Remove the left
        #     hash2[ord(s2[left])-ord('a')] -=1
        #     left+=1
        # return False

        # Approach 2: Same as approach 1 but we hash into numbers instead of hashMap of 26 characters like Approach 2
        # hash1 = hash2 = 0
        # lenS1 = len(s1)
        # lenS2 = len(s2)
        # if lenS2 < lenS1:
        #     return False
        # right = left = 0
        # while right < lenS1:
        #     hash1 += hash(s1[right])
        #     hash2 += hash(s2[right])
        #     right += 1
        # right -= 1
        # while right < lenS2:
        #     if hash1 == hash2:
        #         return True
        #     right += 1
        #     if right != lenS2:
        #         hash2 += hash(s2[right])
        #     # Remove the left
        #     hash2 -= hash(s2[left])
        #     left += 1
        # return False

        # Approach 3: Optimized solution
        # Time O(n)
        # Space O(n)
        hash1 = hash2 = 0
        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS2 < lenS1:
            return False
        for i in range(lenS1):
            hash1 += hash(s1[i])
            hash2 += hash(s2[i])
        if hash1 == hash2:
            return True
        for j in range(lenS2 - lenS1):
            # hash2
            hash2 = hash2 + hash(s2[j + lenS1]) - hash(s2[j])
            if hash2 == hash1:
                return True
        return False