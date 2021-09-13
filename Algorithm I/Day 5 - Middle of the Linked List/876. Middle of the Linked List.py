# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 0: two pointer but slow :)
        # Time O(n)
        # Space O(1)
        # count = 0
        # fast = head
        # slow = head
        # while fast:
        #     fast = fast.next
        #     count+=1
        # mid = count//2
        # while mid>0:
        #     slow = slow.next
        #     mid-=1
        # return slow

        # Approach 1: Output to Array
        # Time O(n)
        # Space O(n)-> used by tempt arr
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

        # Approach 2: Two pointers
        # Time O(n)
        # Space O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow