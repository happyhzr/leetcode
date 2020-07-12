class Solution:
    def numIdenticalPairs(self, nums):
        hash = {}
        for i in range(len(nums)):
            if not hash.get(nums[i]):
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

        ans = 0
        for k in hash:
            ans += self.cnk(hash[k], 2)
        return int(ans)

    def f(self, n):
        res = 1
        i = 1
        while i <= n:
            res *= i
            i += 1
        return res

    def cnk(self, n, k):
        if n < k:
            return 0
        return self.f(n)/(self.f(n-k)*self.f(k))


if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 1, 1, 3]
    ans = s.numIdenticalPairs(nums)
    print(ans)

    nums = [1, 1, 1, 1]
    ans = s.numIdenticalPairs(nums)
    print(ans)

    nums = [1, 2, 3]
    ans = s.numIdenticalPairs(nums)
    print(ans)
