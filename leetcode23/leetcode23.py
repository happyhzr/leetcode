#!/usr/bin/env python


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        interval = 1
        while interval < len(lists):
            i = 0
            while i + interval < len(lists):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
                i += 2 * interval
            interval *= 2

        if len(lists) == 0:
            return None
        return lists[0]

    def merge2Lists(self, l1, l2):
        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return head.next


a1 = ListNode(-1)
a2 = ListNode(1)

b1 = ListNode(-3)
b2 = ListNode(1)
b3 = ListNode(4)

c1 = ListNode(-2)
c2 = ListNode(-1)
c3 = ListNode(0)
c4 = ListNode(2)

a1.next = a2

b1.next = b2
b2.next = b3

c1.next = c2
c2.next = c3
c3.next = c4

s = Solution()
head = s.mergeKLists([a1, b1, c1])
while head:
    print 'val:', head.val
    head = head.next
