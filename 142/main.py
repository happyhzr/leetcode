from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if slow is None:
                raise Exception("impossible: slow is none")
            slow = slow.next
            if fast == slow:
                p = fast
                q = head
                while p != q:
                    if p is None:
                        raise Exception("impossible: p is none")
                    p = p.next
                    if q is None:
                        raise Exception("impossible: q is none")
                    q = q.next
                return p
        return None
