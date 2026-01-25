class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)
        for i in range(0, len(lst), 2 * k):
            if i + k - 1 < len(lst):
                lst[i : i + k] = self.reverse(lst[i : i + k])
            else:
                lst[i:] = self.reverse(lst[i:])
        return "".join(lst)

    def reverse(self, lst: list[str]) -> list[str]:
        start = 0
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        return lst


if __name__ == "__main__":
    s = Solution()
    print(s.reverseStr("abcdefg", 2))  # Output: "bacdfeg"
    print(s.reverseStr("abcd", 2))  # Output: "bacd"
