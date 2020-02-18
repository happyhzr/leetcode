class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x//10

        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    x = 121
    ans = s.isPalindrome(x)
    print(ans)
