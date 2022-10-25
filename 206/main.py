from typing import Optional, List


class ListNode:
    val: int
    next: Optional

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def new_list(self, lst: List[int]):
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

    def get_list(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst


if __name__ == '__main__':
    s = Solution()
    head = s.new_list([1, 2, 3, 4, 5])
    head = s.reverseList(head)
    print(s.get_list(head))

    head = s.new_list([1, 2])
    head = s.reverseList(head)
    print(s.get_list(head))

    head = s.new_list([])
    head = s.reverseList(head)
    print(s.get_list(head))
