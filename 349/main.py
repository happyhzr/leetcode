class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash = [0] * 1001
        for n in nums1:
            hash[n] = 1
        result = set()
        for n in nums2:
            if hash[n] == 1:
                result.add(n)
        return list(result)
