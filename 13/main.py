class Solution:
    def romanToInt(self, s):
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in mapping:
                res += mapping[s[i:i+2]]
                i += 2
            else:
                res += mapping[s[i]]
                i += 1
        return res


if __name__ == '__main__':
    sl = Solution()
    s = 'III'
    i = sl.romanToInt(s)
    print(i)

    s = 'IV'
    i = sl.romanToInt(s)
    print(i)

    s = 'IX'
    i = sl.romanToInt(s)
    print(i)

    s = 'LVIII'
    i = sl.romanToInt(s)
    print(i)
