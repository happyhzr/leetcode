from typing import Optional, List


class ListNode:
    val: int
    next: Optional

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def new_list(self, lst: List[int]) -> Optional[ListNode]:
        head = None
        tail = head
        for v in lst:
            if head is None:
                head = ListNode(v, None)
                tail = head
            elif head == tail:
                tail = ListNode(v, None)
                head.next = tail
            else:
                node = ListNode(v, None)
                tail.next = node
                tail = tail.next
        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        dummy.next = head
        t = dummy
        while t.next is not None:
            if t.next.val == val:
                t.next = t.next.next
            else:
                t = t.next
        return dummy.next

    def get_list(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst


if __name__ == '__main__':
    s = Solution()
    head = s.new_list([1, 2, 3, 4, 5, 6])
    head = s.removeElements(head, 6)
    print(s.get_list(head))
    head = s.new_list([])
    head = s.removeElements(head, 1)
    print(s.get_list(head))
    head = s.new_list([7, 7, 7, 7])
    head = s.removeElements(head, 7)
    print(s.get_list(head))
