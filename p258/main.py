class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.add(num)
        return num

    def add(self, num: int) -> int:
        result = 0
        while num != 0:
            result += num % 10
            num //= 10
        return result
