class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = len(s)-1
        l = 0
        while i >= 0:
            if s[i] == ' ':
                break
            else:
                l += 1
            i -= 1
        return l


if __name__ == '__main__':
    solution = Solution()

    s = ''
    print(solution.lengthOfLastWord(s))

    s = 'Hello World'
    print(solution.lengthOfLastWord(s))

    s = 'a '
    print(solution.lengthOfLastWord(s))
