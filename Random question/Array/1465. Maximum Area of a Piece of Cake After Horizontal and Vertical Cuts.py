class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        # Approach: Implementation
        # Time O(nlogn) # sort arrays
        # Space O(n)
        # Base on https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/661995/Do-you-like-visual-explanation-You-got-it.-%3A-)-With-2-code-variations.
        hCuts.sort(), vCuts.sort()
        
        # Horizontal cut lengths
        h_lengths = [hCuts[0]]
        for i in range(1, len(hCuts)):
            h_lengths.append(hCuts[i] - hCuts[i-1])
        h_lengths.append(h - hCuts[-1])
        
        # Vertical cut lengths
        v_lengths = [vCuts[0]]
        for i in range(1, len(vCuts)):
            v_lengths.append(vCuts[i] - vCuts[i-1])
        v_lengths.append(w - vCuts[-1])
        
        
        max_h = max(h_lengths)
        max_v = max(v_lengths)
        
        mod = 10**9 + 7
        return int((max_h * max_v)%mod)
        
        