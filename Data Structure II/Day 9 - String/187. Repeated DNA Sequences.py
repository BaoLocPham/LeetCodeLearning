class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Approach 1: Hash Map Brute Force -> TLE for python T.T
        # Time O(n^2)
        # Space O(n)
        # ans = set()
        # for i in range(len(s)-9):
        #     ss = s[i:i+10]
        #     if ss not in ans:
        #         for j in range(i+1, len(s)-9):
        #             sx = s[j:j+10]
        #             if ss==sx:
        #                 ans.add(ss)
        #                 break
        # return list(ans)

        # Approach 2: Rolling Hash
        # Time O(n)
        # Space O(n)
        hashMap = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        words = set()
        doubleWords = set()
        rs = []
        for i in range(len(s) - 9):
            v = 0
            for j in range(i, i + 10):
                v <<= 2
                v += hashMap[s[j]]
            if v in words:
                if v not in doubleWords:
                    doubleWords.add(v)
                    rs.append(s[i: i + 10])
            words.add(v)
        return rs