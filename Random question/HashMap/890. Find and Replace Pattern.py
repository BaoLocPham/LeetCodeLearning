class Solution:
    # Approach 1: Two hash map
    # Time O(N*K) N is number of words, K is length of each word
    # Space O(N*K)
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def solve(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        return filter(solve, words)