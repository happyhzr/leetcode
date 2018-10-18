class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for x in nums:
            t = []
            for y in subsets:
                t.append(y+[x])
            subsets.extend(t)
        return subsets


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    subsets = s.subsets(nums)
    print(subsets)
