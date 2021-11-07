class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Approach 1: using queue for move and remove player
        # Time O(n*k) n: number of players
        # Space O(n)
        queue = [x+1 for x in range(n)]
        while len(queue)>1:
            x = k
            while x>1:
                x-=1
                front = queue[0]
                # pop the first and then push it to the back of the queue
                queue.pop(0)
                queue.append(front)
            # remove the kth player
            queue.pop(0)
        return queue[0]
        # Approach 2: using magic solution
        # Well, how can he come up with this solution?
        # Time O(n)
        # Space O(1)
        # https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/1152705/JavaC%2B%2BPython-4-lines-O(n)-time-O(1)-space
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1