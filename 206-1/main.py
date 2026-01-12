from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev: ListNode | None = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
