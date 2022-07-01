class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Approach 1: Using set
        # Time O(nk^2) # subarray of a word k, discard k 
        # Space O(nk)
        setW = set(words)
        for w in words:
            for i in range(1, len(w)):
                setW.discard(w[i:]) # remove suffix from the set of words
        return sum(len(w) + 1 for w in setW) # plus 1 because of the '#' character
        
# Approach 2: Trie
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.ends = [] # store all encoded words
    
    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        self.ends.append((cur, len(word) + 1)) # +1 for the '#' character
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for w in set(words):
            trie.insert(w[::-1])
        
        return sum(length for node, length in trie.ends if len(node.children) == 0)