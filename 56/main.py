class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=self.cmp)
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result

    def cmp(self, x: list[int]) -> int:
        return x[0]
