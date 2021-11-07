class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Approach 1: using temp string for rs
        # Time O(n)
        # Space O(n)
        opening, ss = 0, []
        # forward loop
        # append only balance parentheses
        for c in s:
            if c == "(":
                opening += 1
            elif c == ")":
                if opening == 0: continue
                opening -= 1
            ss.append(c)

        # backward loop
        # remove left over opening parenthese
        rs = []
        for i in range(len(ss) - 1, -1, -1):
            if opening > 0 and ss[i] == "(":
                opening -= 1
                continue
            rs.append(ss[i])
        return "".join(rs[::-1])

        # Approach 2: using stack
        # Time O(n)
        # Space O(n)
        ss, stack = list(s), []
        # first loop for handle balance parentheses
        for i, c in enumerate(ss):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    ss[i] = ""
        # second loop for handle leftover opening parenthese
        while stack:
            ss[stack.pop()] = ""
        return "".join(ss)