
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(' ')
    hashMap = {}
    if len(words)!=len(pattern):
        return False
    for i in range(len(words)):

        if hashMap.get(pattern[i], 0)!=hashMap.get(words[i], 0):
            return False
        hashMap[pattern[i]] = i
        hashMap[words[i]] = i
    return True

pattern="abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))