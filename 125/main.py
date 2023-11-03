class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if ord(c) >= ord("A") and ord(c) <= ord("Z"):
                new_s += chr(ord(c) + ord("a") - ord("A"))
            elif ord(c) >= ord("a") and ord(c) <= ord("z"):
                new_s += c
            elif ord(c) >= ord("0") and ord(c) <= ord("9"):
                new_s += c
        return new_s == new_s[::-1]
