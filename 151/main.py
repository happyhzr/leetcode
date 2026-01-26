class Solution:
    def reverseWords(self, s: str) -> str:
        a = list(s)
        a = self.remove(a)
        print("".join(a))
        a.reverse()
        start = 0
        for i in range(len(a) + 1):
            if i == len(a) or a[i] == " ":
                a[start:i] = reversed(a[start:i])
                start = i + 1
        return "".join(a)

    def remove(self, a: list[str]) -> list[str]:
        fast = 0
        slow = 0
        while fast < len(a):
            if a[fast] != " ":
                if slow != 0:
                    a[slow] = " "
                    slow += 1
                while fast < len(a) and a[fast] != " ":
                    a[slow] = a[fast]
                    fast += 1
                    slow += 1
            fast += 1
        a = a[:slow]
        return a


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("  Bob    Loves  Alice   "))  # "Alice Loves Bob"
