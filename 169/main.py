from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        for v in nums:
            if v in cache:
                cache[v] += 1
            else:
                cache[v] = 1
        for k, v in cache.items():
            if v > len(nums) // 2:
                return k
        raise Exception("impossible")