class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1: sorted string + hashMap
        # Time O(nlogn)
        # Space O(n)
        ans = {}
        for word in strs:
            w = ''.join(sorted(word))
            if ans.get(w, 0)==0:
                ans[w] = [word]
            else:
                ans[w].append(word)
        return ans.values()