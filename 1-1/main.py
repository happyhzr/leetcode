class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, v in enumerate(nums):
            another = target - v
            if another in dict:
                j = dict.get(another)
                if j is None:
                    raise Exception("No two sum solution")
                return [j, i]
            dict[v] = i
        raise Exception("No two sum solution")
