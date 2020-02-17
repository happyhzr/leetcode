import sys


class Solution:
    def reverse(self, x):
        if x == 0:
            return x

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        xs = []
        while x > 0:
            xs.append(x % 10)
            x = x//10

        i = 0
        while xs[i] == 0:
            i += 1

        j = i
        r = 0
        while j <= len(xs)-1:
            r = 10*r+xs[j]
            j += 1

        r = sign*r

        if r < -2**31-1 or r > 2**31:
            return 0
        return r


if __name__ == '__main__':
    s = Solution()
    x = 1534236469
    r = s.reverse(x)
    print(r)
    print(2**31)
