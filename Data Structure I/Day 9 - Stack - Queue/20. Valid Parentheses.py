class Solution:
    def is_common(self, p1, p2) -> bool:
        # Helper function for approach 2: more verbose :(
        if p1 == "(" and p2 == ")":
            return True
        if p1 == "[" and p2 == "]":
            return True
        if p1 == "{" and p2 == "}":
            return True
        return False
    def isValid(self, s: str) -> bool:
        # this problem is basically a stack-use problem
        # Approach 1: using dict
        # Time O(n)
        # Space O(n) size of the stack
        # stack = []
        # dict = {"]": "[", "}": "{", ")": "("}
        # for ss in s:
        #     if ss in dict.values():
        #         stack.append(ss)
        #     elif ss in dict.keys():
        #         if len(stack) == 0 or dict[ss] != stack.pop(-1):
        #             return False
        # return stack == []
        # Approach 2:
        stack = []
        for ss in s:
            if ss in "([{":
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                if self.is_common(stack[-1], ss):
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False