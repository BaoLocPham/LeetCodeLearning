class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        hashMap = {}
        if len(words)!=len(pattern):
        return False
        for i in range(len(words)):
        if hashMap.get(pattern[i])!=hashMap.get(words[i]):
        return False
        hashMap[pattern[i]] = i
        hashMap[words[i]] = i
        return True