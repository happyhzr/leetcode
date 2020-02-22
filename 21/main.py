# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        tail = head

        while(True):
            if(l1 == None):
                tail.next = l2
                break
            elif(l2 == None):
                tail.next = l1
                break

            if(l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        return head.next

    def convert_array_to_list(self, a):
        head = None
        tail = None
        for e in a:
            if head == None:
                head = ListNode(e)
                tail = head
            else:
                node = ListNode(e)
                tail.next = node
                tail = node
        return head

    def print_list(self, l):
        while l:
            print(l.val, end=' ')
            l = l.next
        print('\n')


if __name__ == '__main__':
    s = Solution()

    a1 = [1, 2, 4]
    a2 = [1, 3, 4]
    l1 = s.convert_array_to_list(a1)
    s.print_list(l1)
    l2 = s.convert_array_to_list(a2)
    s.print_list(l2)
    l = s.mergeTwoLists(l1, l2)
    s.print_list(l)

    a1 = [1, 2, 4]
    a2 = []
    l1 = s.convert_array_to_list(a1)
    s.print_list(l1)
    l2 = s.convert_array_to_list(a2)
    s.print_list(l2)
    l = s.mergeTwoLists(l1, l2)
    s.print_list(l)

    a1 = []
    a2 = [1, 3, 4]
    l1 = s.convert_array_to_list(a1)
    s.print_list(l1)
    l2 = s.convert_array_to_list(a2)
    s.print_list(l2)
    l = s.mergeTwoLists(l1, l2)
    s.print_list(l)

    a1 = []
    a2 = []
    l1 = s.convert_array_to_list(a1)
    s.print_list(l1)
    l2 = s.convert_array_to_list(a2)
    s.print_list(l2)
    l = s.mergeTwoLists(l1, l2)
    s.print_list(l)
