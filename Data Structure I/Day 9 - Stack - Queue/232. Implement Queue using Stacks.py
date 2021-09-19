class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1, self.s2 = [], []
    # This approach
    # O(n) - push
    # O(1) - pop
    # def push(self, x: int) -> None:
    #     """
    #     Push element x to the back of queue.
    #     """
    #     while self.s1:
    #         self.s2.append(self.s1.pop(0))
    #     self.s2.append(x)
    #     while self.s2:
    #         self.s1.append(self.s2.pop(0))
    #
    # def pop(self) -> int:
    #     """
    #     Removes the element from in front of queue and returns that element.
    #     """
    #     return self.s1.pop(0)
    #
    # def peek(self) -> int:
    #     """
    #     Get the front element.
    #     """
    #     return self.s1[0]
    #
    # def empty(self) -> bool:
    #     """
    #     Returns whether the queue is empty.
    #     """
    #     return self.s1 == []
    #
    # This approach
    # O(1) - push
    # O(1) - pop
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2

    def move(self):
        """
        Move elements from inStack (s1) to outStack(s2)
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()