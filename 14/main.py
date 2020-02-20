class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        c = strs[0]
        l = len(c)
        for i in range(len(strs)):
            if len(strs[i]) < l:
                l = len(strs[i])

        prefix = ''
        for i in range(l):
            for j in range(len(strs)):
                if c[i] != strs[j][i]:
                    return prefix
            prefix += (c[i])

        return prefix


if __name__ == '__main__':
    s = Solution()

    strs = ["flower", "flow", "flight"]
    prefix = s.longestCommonPrefix(strs)
    print(prefix)

    strs = ["dog", "racecar", "car"]
    prefix = s.longestCommonPrefix(strs)
    print(prefix)
