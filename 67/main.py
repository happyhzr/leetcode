class Solution:
    def addBinary(self, a, b):
        l = max(len(a), len(b))
        res = [0]*l
        i = len(a)-1
        j = len(b)-1
        k = len(res)-1

        while i >= 0 and j >= 0:
            res[k] = str(int(a[i])+int(b[j]))
            i -= 1
            j -= 1
            k -= 1

        while i >= 0:
            res[k] = a[i]
            i -= 1
            k -= 1

        while j >= 0:
            res[k] = b[j]
            j -= 1
            k -= 1

        c = 0
        i = l-1
        while i >= 0:
            n = int(res[i])+c
            c = n // 2
            n %= 2
            res[i] = str(n)
            i -= 1

        if c == 1:
            res.insert(0, '1')

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()

    a = '11'
    b = '1'
    print(s.addBinary(a, b))

    a = '1010'
    b = '1011'
    print(s.addBinary(a, b))

    a = '1'
    b = '111'
    print(s.addBinary(a, b))

    a = '1111'
    b = '1111'
    print(s.addBinary(a, b))
