# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = self.get_num(l1)
        n2 = self.get_num(l2)
        print('n1: {}, n2; {}'.format(n1, n2))
        n = n1+n2
        return self.get_list(n)

    def get_num(self, l):
        nums = []
        while l:
            nums.append(l.val)
            l = l.next
        num = 0
        i = len(nums)-1
        while i >= 0:
            num = num*10+nums[i]
            i -= 1
        return num

    def get_list(self, num):
        nums = []
        while num > 0:
            nums.append(num % 10)
            num = num // 10
        if len(nums) == 0:
            nums = [0]
        dummy = ListNode(0)
        i = len(nums)-1
        while i >= 0:
            node = ListNode(nums[i])
            node.next = dummy.next
            dummy.next = node
            i -= 1
        return dummy.next

    def insert_into_list(self, nums):
        dummy = ListNode(0)
        for i in range(len(nums)):
            node = ListNode(nums[i])
            node.next = dummy.next
            dummy.next = node
        return dummy.next


if __name__ == '__main__':
    n1 = [0]
    n2 = [0]
    s = Solution()
    l1 = s.insert_into_list(n1)
    l2 = s.insert_into_list(n2)
    ans = s.addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next
