# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        second = dummy
        first = dummy
        i = 0

        while i < n:
            first = first.next
            i += 1

        if first.next is None:
            return head.next   # n == length, head itself is removed

        while first.next is not None:
            second = second.next
            first = first.next

        second.next = second.next.next
        return head