from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr is not None and curr.next is not None and curr.next.next is not None:
            temp = curr.next
            temp1 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = temp
            temp.next = temp1
            curr = curr.next.next
        if dummy is not None:
            return dummy.next
