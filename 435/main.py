class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key=self.cmp)
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                count += 1
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])
        return count

    def cmp(self, x: list[int]) -> int:
        return x[0]
