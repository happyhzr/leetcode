class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()

    haystack = 'hello'
    needle = 'll'
    print(s.strStr(haystack, needle))

    haystack = 'aaaaa'
    needle = 'bba'
    print(s.strStr(haystack, needle))
