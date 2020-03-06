# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head

        pre = head
        current = head.next
        while current:
            if current.val == pre.val:
                pre.next = current.next
            else:
                pre = pre.next
            current = current.next
        return head

    def get_list_from_array(self, a):
        d = ListNode(0)
        for i in range(len(a)-1, 0, -1):
            node = ListNode(a[i])
            node.next = d.next
            d.next = node
        return d.next

    def print_list(self, head):
        while head:
            print(head.val, end=' ')
            head = head.next
        print()


if __name__ == '__main__':
    s = Solution()

    a = [1, 1, 2]
    s.print_list(s.deleteDuplicates(s.get_list_from_array(a)))

    a = [1, 1, 2, 3, 3]
    s.print_list(s.deleteDuplicates(s.get_list_from_array(a)))
