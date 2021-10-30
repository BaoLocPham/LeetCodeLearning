class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Approach 1: iteration
        # Time O(n)
        # Space O(n)
        num1, num2 = list(num1), list(num2)
        res, carry = [], 0
        while len(num1)>0 or len(num2)>0:
            # convert str to int
            n1 = ord(num1.pop())-ord('0') if len(num1)>0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2)>0 else 0
            tmp = n1+n2+carry
            res.append(str(tmp%10))
            carry = tmp//10
        if carry: res.append('1')
        return ''.join(res[::-1])

        # Approach 2: Lazy
        # Time O(n)
        # Space O(1)
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 + num2)