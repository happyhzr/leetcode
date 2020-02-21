class Solution:
    def is_match(self, l, r):
        if l == '(' and r == ')':
            return True
        if l == '[' and r == ']':
            return True
        if l == '{' and r == '}':
            return True
        return False

    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) == 0:
                    return False
                c = stack.pop()
                if not self.is_match(c, s[i]):
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()

    s = '()'
    ans = solution.isValid(s)
    print(ans)

    s = '()[]{}'
    ans = solution.isValid(s)
    print(ans)

    s = '(]'
    ans = solution.isValid(s)
    print(ans)

    s = '([)]'
    ans = solution.isValid(s)
    print(ans)

    s = '{[]}'
    ans = solution.isValid(s)
    print(ans)
