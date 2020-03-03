class Solution:
    def plusOne(self, digits):
        i = len(digits)-1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
            i -= 1

        if i == -1:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    s = Solution()

    digits = [1, 2, 3]
    print(s.plusOne(digits))

    digits = [4, 3, 2, 1]
    print(s.plusOne(digits))

    digits = [8]
    print(s.plusOne(digits))

    digits = [9]
    print(s.plusOne(digits))
