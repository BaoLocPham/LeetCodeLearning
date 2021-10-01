class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Approach 1: Using stack
        # Time O(n)
        # Space O(n)
        def build(s:str):
            st = []
            for ch in s:
                if ch=="#" and st:
                    st.pop()
                elif ch!="#":
                    st.append(ch)
            return st
        return build(s)==build(t)

        # Approach 2: using Two Pointers ver Lazy
        # Time O(n)
        # Space O(1)
        def build(S):
            skip = 0
            for x in reversed(S):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(build(s), build(t)))

        # Approach 3: using Two Pointers ver faster, yet longer code :)
        # Time O(n)
        # Space O(1)
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >= 0:  # Find the next possible char in build(s)
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:  # Find the next possible char in build(t)
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT:
                    skipT -= 1
                    j -= 1
                else:
                    break
            # if two actual characters are different
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            # if expecting to compare char vs nothing
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True