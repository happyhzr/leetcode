from heapq import heapify, heappush, heappop


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 0
        array = []
        for key, v in map.items():
            heappush(array, (v, key))
            if len(array) > k:
                heappop(array)
        result = [0] * k
        for i in reversed(range(0, k)):
            pair = heappop(array)
            result[i] = pair[1]
        return result
