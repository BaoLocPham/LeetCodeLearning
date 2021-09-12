class Solution:
    def reverseWords(self, s: str) -> str:
        # two pointer ~ 122ms
        s = s.split(" ")
        for i,word in enumerate(s):
            l = 0
            r = len(word)-1
            word = list(word)
            while l<r:
                word[r], word[l] = word[l], word[r]
                l, r = l+1, r-1
        return " ".join(s)
        
        # list comprehension ~ 28ms
        #return " ".join([x[::-1] for x in s.split(" ")])