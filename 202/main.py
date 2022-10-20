class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        slow = self.helper(slow)
        fast = self.helper(fast)
        fast = self.helper(fast)
        while True:
            if fast == 1:
                return True
            if fast == slow:
                return False
            print(slow)
            slow = self.helper(slow)
            fast = self.helper(fast)
            fast = self.helper(fast)

    def helper(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
