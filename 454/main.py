class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        count = 0
        dict = {}
        for a in nums1:
            for b in nums2:
                dict[a + b] = dict.get(a + b, 0) + 1
        for c in nums3:
            for d in nums4:
                count += dict.get(-c - d, 0)
        return count
