from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            if fast is None:
                break
            fast = fast.next
        while fast is not None:
            fast = fast.next
            if slow is None:
                raise Exception("slow is none")
            slow = slow.next
        if slow is None:
            raise Exception("slow is none")
        if slow.next is None:
            raise Exception("slow.next is none")
        slow.next = slow.next.next
        return dummy.next
