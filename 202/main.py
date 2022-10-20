class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while True:
            print(n)
            if n == 1:
                return True
            if n in cache:
                return False
            cache.add(n)
            n = self.helper(n)

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
